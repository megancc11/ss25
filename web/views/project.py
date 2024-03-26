#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

from web.forms.project import ProjectModelForm
from web import models
from django.conf import settings

from utils.tencent.cos import create_bucket

def project_list(request):
    """ 项目列表 """
    if request.method == "GET":
        # GET请求查看项目列表
        """
        1. 从数据库中获取两部分数据
            我创建的所有项目：已星标star、未星标my
            我参与的所有项目：已星标star、未星标my
        2. 提取已星标
            列表 = 循环 [我创建的所有项目] + [我参与的所有项目] 把已星标的数据提取

        得到三个列表：星标、创建、参与
        """
        project_dict = {'star': [], 'my': [], 'join': []}

        # 我创建的所有项目
        my_project_list = models.Project.objects.filter(creator=request.tracer.user)
        for row in my_project_list:
            if row.star:
                #已星标
                project_dict['star'].append({"value": row, 'type': 'my'})#type用于区分自己创建的项目还是加入别人创建的项目
            else:
                project_dict['my'].append(row)

        #我参与的所有项目
        join_project_list = models.ProjectUser.objects.filter(user=request.tracer.user)

        for item in join_project_list:
            if item.star:
                project_dict['star'].append({"value": item.project, 'type': 'join'})#item.project加入参与的项目而不是对象，#type用于区分自己创建的项目还是加入别人创建的项目
            else:
                project_dict['join'].append(item.project)
        # print(project_dict)

        form = ProjectModelForm(request)
        return render(request, 'web/project_list.html', {'form': form, 'project_dict': project_dict})

    # POST，对话框的ajax添加项目。
    form = ProjectModelForm(request, data=request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        # 1. 为项目创建一个桶,桶的命名规则：用户邮箱前缀+当前时间戳+桶后缀字符串,不能加项目名称因为桶命不支持中文，存储桶名称必须由数字、小写字母和 - 组成
        bucket = "{}-{}".format(request.tracer.user.email.split("@")[0], str(int(time.time())))+settings.BUCKET_SUFFIX
        region = 'ap-chengdu'
        create_bucket(bucket, region)

        # 2.创建项目
        # 验证通过：项目名、颜色、描述 + creator谁创建的项目？
        form.instance.bucket = bucket
        form.instance.region = region
        form.instance.creator = request.tracer.user
        instance = form.save()

        #3.项目初始化问题类型
        issues_type_object_list = []
        for item in models.IssuesType.PROJECT_INIT_LIST:  # ["任务", '功能', 'Bug']
            issues_type_object_list.append(models.IssuesType(project=instance, title=item))
        models.IssuesType.objects.bulk_create(issues_type_object_list)

        return JsonResponse({'status': True})

    return JsonResponse({'status': False, 'error': form.errors})

def project_star(request, project_type, project_id):
    # """ 星标项目 """
    if project_type == 'my':
        models.Project.objects.filter(id=project_id, creator=request.tracer.user).update(star=True)
        return redirect('project_list')

    if project_type == 'join':
        models.ProjectUser.objects.filter(project_id=project_id, user=request.tracer.user).update(star=True)
        return redirect('project_list')

    return HttpResponse('请求错误')


def project_unstar(request, project_type, project_id):
    """ 取消星标 """
    if project_type == 'my':
        models.Project.objects.filter(id=project_id, creator=request.tracer.user).update(star=False)
        return redirect('project_list')

    if project_type == 'join':
        models.ProjectUser.objects.filter(project_id=project_id, user=request.tracer.user).update(star=False)
        return redirect('project_list')

    return HttpResponse('请求错误')

def upload_js(request):
    return render(request, 'web/js测试.html')
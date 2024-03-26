from django.urls import path
from django.conf.urls import url
from web.views import account,home,project,dashboard,wiki,file,setting,issues,statistics

#前端写URL时需要加上web/
urlpatterns = [
    path('index/', home.index, name='index'),
    path('sms/send/', account.send_sms),
    path('register/', account.register, name='register'),
    path('login/', account.login, name='login'),
    path('logout/', account.logout, name='logout'),
    path('image/code/', account.image_code, name='image_code'),
    path('login/email/', account.login_email, name='loginemail'),
    path('send/email/', account.send_email, name='send_email'),

    #支付
    path('price/', home.price, name='price'),
    path('payment/<policy_id>', home.payment, name='payment'),
    path('pay/', home.pay, name='pay'),
    path('pay/notify/', home.pay_notify, name='pay_notify'),
    # url(r'^price/$', home.price, name='price'),
    # url(r'^payment/(?P<policy_id>\d+)/$', home.payment, name='payment'),
    # url(r'^pay/$', home.pay, name='pay'),
    # url(r'^pay/notify/$', home.pay_notify, name='pay_notify'),

    #项目列表
    path('project/list/', project.project_list, name='project_list'),
    path('project/star/<project_type>/<project_id>',project.project_star, name='project_star'),
    path('project/unstar/<project_type>/<project_id>',project.project_unstar, name='project_unstar'),
    path('project/upload_js/', project.upload_js, name='upload_js'),


    # 项目概览
    path('manage/dashboard/<project_id>', dashboard.dashboard, name='dashboard'),
    path('manage/issues/chart/<project_id>', dashboard.issues_chart, name='issues_chart'),

    # url(r'^dashboard/$', dashboard.dashboard, name='dashboard'),
    # url(r'^dashboard/issues/chart/$', dashboard.issues_chart, name='issues_chart'),

    #项目设置
    path('manage/setting/<project_id>', setting.setting, name='setting'),
    path('manage/setting/delete/<project_id>', setting.delete, name='setting_delete'),

    # url(r'^setting/$', setting.setting, name='setting'),
    # url(r'^setting/delete/$', setting.delete, name='setting_delete'),
    #wiki
    path('manage/wiki/<project_id>', wiki.wiki, name='wiki'),
    path('manage/wiki/add/<project_id>', wiki.wiki_add, name='wiki_add'),
    path('manage/wiki/catalog/<project_id>', wiki.wiki_catalog, name='wiki_catalog'),
    path('manage/wiki/delete/<project_id>/<wiki_id>', wiki.wiki_delete, name='wiki_delete'),
    path('manage/wiki/edit/<project_id>/<wiki_id>', wiki.wiki_edit, name='wiki_edit'),
    path('manage/wiki/upload/<project_id>', wiki.wiki_upload, name='wiki_upload'),
    # url(r'^wiki/$', wiki.wiki, name='wiki'),
    # url(r'^wiki/add/$', wiki.wiki_add, name='wiki_add'),
    # url(r'^wiki/catalog/$', wiki.wiki_catalog, name='wiki_catalog'),
    # url(r'^wiki/delete/(?P<wiki_id>\d+)/$', wiki.wiki_delete, name='wiki_delete'),
    # url(r'^wiki/edit/(?P<wiki_id>\d+)/$', wiki.wiki_edit, name='wiki_edit'),
    # url(r'^wiki/upload/$', wiki.wiki_upload, name='wiki_upload'),

    #问题管理
    path('manage/issues/<project_id>', issues.issues, name='issues'),
    path('manage/issues/detail/<project_id>/<issues_id>', issues.issues_detail, name='issues_detail'),
    path('manage/issues/record/<project_id>/<issues_id>', issues.issues_record, name='issues_record'),
    path('manage/issues/change/<project_id>/<issues_id>', issues.issues_change, name='issues_change'),
    path('manage/issues/invite/<project_id>', issues.invite_url, name='invite_url'),
    path('manage/issues/join/<code>', issues.invite_join, name='invite_join'),

    # url(r'^issues/$', issues.issues, name='issues'),
    # url(r'^issues/detail/(?P<issues_id>\d+)/$', issues.issues_detail, name='issues_detail'),
    # url(r'^issues/record/(?P<issues_id>\d+)/$', issues.issues_record, name='issues_record'),
    # url(r'^issues/change/(?P<issues_id>\d+)/$', issues.issues_change, name='issues_change'),
    # url(r'^issues/invite/url/$', issues.invite_url, name='invite_url'),
    path('invite/join/<code>', issues.invite_join, name='invite_join'),
    # url(r'^invite/join/<code>/$', issues.invite_join, name='invite_join'),

    #文件操作
    path('manage/file_upload_test/<project_id>', file.file_upload_test, name='file_upload_test'),#测试用

    path('manage/file/<project_id>', file.file, name='file'),
    path('manage/file/delete/<project_id>', file.file_delete, name='file_delete'),
    path('manage/file/credential/<project_id>', file.cos_credential, name='cos_credential'),
    path('manage/file/credential_test/<project_id>', file.cos_credential_test, name='cos_credential_test'),
    path('manage/file/post/<project_id>', file.file_post, name='file_post'),
    path('manage/file/download/<project_id>/<file_id>', file.file_download, name='file_download'),
    # url(r'^file/$', file.file, name='file'),
    # url(r'^file/delete/$', file.file_delete, name='file_delete'),
    # url(r'^cos/credential/$', file.cos_credential, name='cos_credential'),
    # url(r'^file/post/$', file.file_post, name='file_post'),
    # url(r'^file/download/(?P<file_id>\d+)/$', file.file_download, name='file_download'),

    #统计
    path('manage/statistics/<project_id>', statistics.statistics, name='statistics'),
    path('manage/statistics/<project_id>', statistics.statistics_priority, name='statistics_priority'),
    path('manage/statistics/<project_id>', statistics.statistics_project_user, name='statistics_project_user'),
    # url(r'^statistics/$', statistics.statistics, name='statistics'),
    # url(r'^statistics/priority/$', statistics.statistics_priority, name='statistics_priority'),
    # url(r'^statistics/project/user/$', statistics.statistics_project_user, name='statistics_project_user'),



]

from django.urls import path
from web.views import account,home,project,dashboard,wiki

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

    #项目列表
    path('project/list/', project.project_list, name='project_list'),
    path('project/star/<project_type>/<project_id>',project.project_star, name='project_star'),
    path('project/unstar/<project_type>/<project_id>',project.project_unstar, name='project_unstar'),


    #项目管理
    path('manage/dashboard/<project_id>', dashboard.dashboard, name='dashboard'),
    path('manage/wiki/<project_id>', wiki.wiki, name='wiki'),
    path('manage/wiki_add/<project_id>', wiki.wiki_add, name='wiki_add'),
    path('manage/catalog/<project_id>', wiki.wiki_catalog, name='wiki_catalog'),
    path('manage/delete/<project_id><wiki_id>', wiki.wiki_delete, name='wiki_delete'),
    path('manage/edit/<project_id><wiki_id>', wiki.wiki_edit, name='wiki_edit'),
    path('manage/upload/<project_id>', wiki.wiki_upload, name='wiki_upload'),
        # url(r'^wiki/$', wiki.wiki, name='wiki'),
        # url(r'^wiki/add/$', wiki.wiki_add, name='wiki_add'),
        # url(r'^wiki/catalog/$', wiki.wiki_catalog, name='wiki_catalog'),
        # url(r'^wiki/delete/(?P<wiki_id>\d+)/$', wiki.wiki_delete, name='wiki_delete'),
        # url(r'^wiki/edit/(?P<wiki_id>\d+)/$', wiki.wiki_edit, name='wiki_edit'),
        # url(r'^wiki/upload/$', wiki.wiki_upload, name='wiki_upload'),

]

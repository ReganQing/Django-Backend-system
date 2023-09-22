"""SimpleERP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings
from web.views import department, user, admin, account, task, parts, chart

urlpatterns = [
    re_path(
        r"media/(?P<path>.*)$",
        serve,
        {"document_root": settings.MEDIA_ROOT},
        name="media",
    ),
    # 部门管理
    path("depart/list/", department.depart_list),
    path("depart/add/", department.depart_add),
    path("depart/<int:nid>/del/", department.depart_del),
    path("depart/<int:nid>/edit/", department.depart_edit),  # 利用正则表达式来进行解析
    path("depart/multi/", department.depart_multi),
    # 员工管理
    path("user/list/", user.user_list),
    path("user/model/form/add/", user.user_add_model_form),
    path("user/<int:nid>/edit/", user.user_edit),
    path("user/<int:nid>/del/", user.user_del),
    # 管理员账户
    path("admin/list/", admin.admin_list),
    path("admin/add/", admin.admin_add),
    path("admin/<int:nid>/edit/", admin.admin_edit),
    path("admin/<int:nid>/del/", admin.admin_del),
    path("admin/<int:nid>/reset/", admin.admin_reset),
    # 用户登录
    path("login/", account.login),
    path("logout/", account.logout),
    path("image/code/", account.image_code),
    path("ajax/task/", task.ajax_task),
    path("ajax/add/", task.ajax_add),
    # 数据统计
    path("chart/list/", chart.chart_list),
    # 零件管理
    path("part/list/", parts.part_list),
    path("part/add/", parts.part_add),
    path("part/<int:nid>/edit/", parts.part_edit),
    path("part/<int:nid>/delete/", parts.part_delete),
    # REST框架的登录和注销视图
    path("", include("api.urls")),
]

"""urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]"""

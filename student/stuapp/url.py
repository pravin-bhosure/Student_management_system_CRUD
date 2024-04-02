from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.login_home,name='loginhome'),
    # path('stu_inner_login', views.stu_inner_login, name='innerlogin'),
    
    path('stu_list', views.stu_list, name='list'),
    # path('stu_add/<int:sub_id>', views.stu_add, name='add'),
    path('stu_add', views.stu_add, name='add'),
    path('stu_filter', views.stu_filter, name='filter'),
    path('stu_delete', views.stu_delete, name='delete'),
    path('stu_delete/<int:stu_id>', views.stu_delete, name='delete'),
    
    path('stu_update/<int:stu_id>', views.update, name='update'),
    path('stu_update/do_update/', views.do_update, name='do_update'),
    path('stu_register', views.stu_register, name='register'),
    path('', views.home, name='home'),
    path('stu_login', views.stu_login, name='login'),
    path('stu_logout', views.stu_logout, name='logout'),
    path('loginin', views.loginin, name='loginin'),
]
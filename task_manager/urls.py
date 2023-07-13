"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from status.views import status_task, create_status, edit_status, delete_status
from labels.views import label, create_label, edit_label, delete_label
from task_manager import views
from .views import index


from tasks.views import edit_tasks, delete_tasks, tasks_list, \
    create_tasks

urlpatterns = [
    path('index/', index, name='index'),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.create_user, name='create_user'),
    path('users/<int:pk>/update/', views.edit_user, name='edit_user'),
    path('users/<int:pk>/delete/', views.delete_user, name='delete_user'),
    path('statuses/', status_task, name='status_task'),
    path('statuses/create/', create_status, name='create_status'),
    path('status/edit/<int:status_id>/', edit_status, name='edit_status'),
    path('status/delete/<int:status_id>/', delete_status, name='delete_status'),
    path('labels/', label, name='label'),
    path('labels/create/', create_label, name='create_label'),
    path('labels/edit/<int:status_id>/', edit_label, name='edit_label'),
    path('delete/<int:label_id>/', delete_label, name='delete_label'),
    path('tasks/', tasks_list, name='tasks'),
    path('tasks/create/', create_tasks, name='create_tasks'),
    path('tasks/edit/<int:task_id>/', edit_tasks, name='edit_tasks'),
    path('tasks/delete/<int:task_id>/', delete_tasks, name='delete_tasks'),

]
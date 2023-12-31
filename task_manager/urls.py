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
from django.urls import path, include

import task_manager
from task_manager.status.views import status_task, create_status, edit_status,\
    delete_status
from task_manager.labels.views import gey_all_labels, \
    create_label, edit_label, delete_label
from task_manager import views
from .views import index

from task_manager.tasks.views import edit_tasks, delete_tasks, tasks_list, \
    create_tasks

urlpatterns = [
    path('index/', index, name='index'),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('users/', include('task_manager.users.urls')),
    path('statuses/', status_task, name='status_task'),
    path('statuses/create/', create_status, name='create_status'),
    path('statuses/<int:status_id>/update/', edit_status, name='edit_status'),
    path('statuses/<int:status_id>/delete/', delete_status,
         name='delete_status'),
    path('labels/', gey_all_labels, name='label'),
    path('labels/create/', create_label, name='create_label'),
    path('labels/<int:status_id>/update/', edit_label, name='edit_label'),
    path('labels/<int:label_id>/delete/', delete_label, name='delete_label'),
    path('tasks/', tasks_list, name='tasks'),
    path('tasks/create/', create_tasks, name='create_tasks'),
    path('tasks/<int:task_id>/update/', edit_tasks, name='edit_tasks'),
    path('tasks/<int:task_id>/delete/', delete_tasks, name='delete_tasks'),
    path('tasks/<int:pk>/', task_manager.tasks.views.TaskDetailsView.as_view(),
         name='tasks_details'),
]

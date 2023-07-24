from django.urls import path
from task_manager.users import views

app_name = 'users'

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('create/', views.create_user, name='create_user'),
    path('<int:pk>/update/', views.UserUpdateFormView.as_view(),
         name='edit_user'),
    path('<int:pk>/delete/', views.delete_user, name='delete_user'),
]

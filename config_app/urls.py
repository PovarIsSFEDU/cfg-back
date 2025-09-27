from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_config_view, name='create'),
    path('deploy/', views.deploy_config_view, name='deploy'),
    path('ask/', views.ask_config_view, name='ask'),
    path('all-configs/', views.get_all_configs_view, name='get_all_configs'),
    path('config-messages/<int:config_id>/', views.get_config_messages_view, name='get_config_messages'),
    path('upload-file/', views.upload_file_view, name='upload_file'),
    path('download-file/<str:filename>/', views.download_file_view, name='download_file'),
]
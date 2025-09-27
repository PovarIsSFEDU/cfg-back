"""
URL configuration for cfg_back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import re_path

@csrf_exempt
def ignore_openai_requests(request):
    # Игнорируем запросы к OpenAI API, которые могут поступать от расширений или других инструментов
    return JsonResponse({'error': 'Not found'}, status=404)

urlpatterns = [
    path('api/', include('config_app.urls')),
    # Игнорируем запросы к OpenAI API
    re_path(r'^v1/models.*$', ignore_openai_requests),  # Ловим все запросы, начинающиеся с /v1/models
]

# Добавляем маршруты для медиафайлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

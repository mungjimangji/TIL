"""firstpjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# urls.py 입장에서는 articles라는 패키지에서
# views라는 모듈을 가져와야함 (패키지이기 땜에 init필요)
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', views.index), # 다름
    # path('articles/', views.index()) # 2번째 인자로 index함수의 반환값이 들어가므로 x 안됨 함수 자체가 들어가야함
    
]

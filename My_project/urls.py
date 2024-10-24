"""
URL configuration for My_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from My_project import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage,name='homepage'),
    path('admin/', admin.site.urls),
    path('about-us/', views.aboutus,name='about-us'),
    path('classes/', views.Classes,name='classes'),
    path('blog/', views.blog,name='blog'),
    path('Passdata/', views.Passdata,name='Passdata'),
    path('calculator/', views.calculator,name='calculator'),
    path('Evenodd/', views.evenodd,name='evenodd'),
    path('examsheet/', views.examsheet,name='examsheet'),
    path('newsdetails/<newname>', views.detail_page),
    path('saveenquiry/', views.saveEnquiry,name='saveenquiry'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

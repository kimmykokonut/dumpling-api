"""
URL configuration for dumplings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from dumplings import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dumplings/', views.dumpling_list), #Index&Create
    path('dumplings/<int:id>', views.dumpling_detail),#Details/update/delete
    path('tags/', views.tag_list),
    path('tags/<int:pk>', views.tag_detail),
    path('origins/', views.origin_list),
    #path('origins/<int:id>', views.origin_detail)

]
# to allow url like dumplings.json
urlpatterns = format_suffix_patterns(urlpatterns)
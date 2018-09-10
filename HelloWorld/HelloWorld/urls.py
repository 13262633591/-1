"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from . import view
from django.conf.urls import *
from . import view,testdb,search,search2

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

# urlpatterns = [
#     # url(r'^$', view.hello),
#     url(r'^$', view.hello_1),
# ]

urlpatterns = [
    url(r'^hello$', view.hello),
    url(r'^testdb_to$', testdb.testdb_to),
    url(r'^testdb_get$', testdb.testdb_get),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search-post$', search2.search_post),
]
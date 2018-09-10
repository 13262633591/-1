"""
HeloWord URL配置



“URLPATH”列表将URL路由到视图。欲了解更多信息，请参见：

HTTPS://DOCS.djangojtup.COM/En/2.1/TopICS/HTTP/URLS//

实例：

功能视图

1。添加导入：从MyIApp导入视图

2。将URL添加到URL模式：路径（‘，VIES.HOLD，Name =’HOST’）

基于类的视图

1。添加导入：从其他App.VIEW导入导入

2。向URL模式添加URL：路径（‘，HOME.ASSVIEW（），Name =‘HOST’）

包括另一个URLCONF

1。导入包含（）函数：从Django.URLS导入包含，路径

2。添加URL模式的URL：路径（‘博客’/’，包括（博客）URL）

HelloWorld URL Configuration

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
    url(r'^admin/', admin.site.urls),
]
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from cmdb import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index),
    url(r'^search_form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^AddInStockBill/$', views.AddInStockBill),
    url(r'^success/$', views.success),
    url(r'^AddItem/$', views.AddItem),
    url(r'^inventoryQuery/$', views.inventoryQuery),
    url(r'^inventoryQueryExtjs/$',views.inventoryQueryExtjs),
    url(r'^getInventoryByItemName/$',views.getInventoryByItemName),
]

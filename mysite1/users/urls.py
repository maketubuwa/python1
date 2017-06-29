from django.conf.urls import url,include
from . import views
urlpatterns = [

    url(r'^$', views.success),
    url(r'^user_login$', views.user_login),
    url(r'^user_logout/$', views.user_logout),
    url(r'^success/$', views.success),
    url(r'^diff_response/$', views.diff_response),
    url(r'^user_only/$', views.user_only),
    url(r'^specific_user/$', views.specific_user),
    url(r'^register/$', views.register),

]

from django.conf.urls import url
from promise import views

urlpatterns = [
    url(r'^promises/$', views.promise_list),
    url(r'^promises/(?P<pk>[0-9]+)/$', views.promise_detail),
]

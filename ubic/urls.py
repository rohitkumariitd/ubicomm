from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]
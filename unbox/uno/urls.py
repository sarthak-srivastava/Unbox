from django.conf.urls import url
from uno import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^q/$', views.exce, name='question'),
]

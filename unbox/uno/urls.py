from django.conf.urls import url
from uno import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^questions/$', views.question, name='question'),
]

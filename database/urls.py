from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^query$', views.query, name='query'),
    url(r'^query_result$', views.query_result, name='query_result'),
    url(r'^button$', views.button, name='button'),
    url(r'^button_result$', views.button_result, name='button_result')

]
from django.conf.urls import patterns, url


from suggest import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^api/$', views.get_cities, name='get_cities'),
)
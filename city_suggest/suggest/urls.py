from django.conf.urls import patterns, url


from suggest import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^api/get_cities/$', views.get_cities, name='get_cities'),
    url(r'^api/get_city_info/$', views.get_city_info, name='get_city_info'),
)

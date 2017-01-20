from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^ninjas/(?P<color>\w+)$', views.whichTurtle), # any word
	# url(r'^/en/(?P<djangoversion>[0-9]\.[0-9])/topics/http/urls/$', views.index)

]

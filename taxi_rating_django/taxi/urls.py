from django.conf.urls import url

from . import views

urlpatterns = [
    # /taxi
    url(r'^$', views.index, name='index')
]

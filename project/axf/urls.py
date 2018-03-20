
from django.conf.urls import url

from . import views

urlpatterns = [
    #home
    url(r'^home/$', views.home),
    #market
    url(r'^market/(\d+)/$', views.market),
    #cart
    url(r'^cart/$', views.cart),
    #mine
    url(r'^mine/$', views.mine),
]

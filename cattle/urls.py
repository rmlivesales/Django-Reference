from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.bill_view, name='bill_view'),
]

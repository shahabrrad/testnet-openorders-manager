from django.conf.urls import url
from . import views

urlpatterns = [
    url('redirect/' , views.landing , name="index"),
    url('slave1/' , views.index1 , name="index1"),
    url('slave2/' , views.index2 , name="index2"),
    url('master/' , views.master_view , name="index3")
]
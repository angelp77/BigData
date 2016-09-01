from django.conf.urls import url, include
from . import views

urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^uno/',views.index1, name='index1'),
url(r'^dos/',views.index, name='index'),
url(r'^upload.html$', views.post_upload, name='post_upload'),
]

# GROUPS URLS.PY
from django.conf.urls import url
from . import views as

app_name = 'groups'

urlpatterns = [
    url('', views.ListGroups.as_view(), name='all'),
    url('new/' views.CreateGroup.as_view(), name='create'),
    url('posts/in/(?P<slug>[-\w]+)/', views.SingleGroup.as_view(), name='single')
    
]

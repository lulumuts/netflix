from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.media_all,name='media_all'),
    
]

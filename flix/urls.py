from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.media_all,name='media_all'),
    url('^search/',views.media_search,name="media_search"),
    url('^details/',views.media_details,name="media_details"),
    url('^list/',views.media_rec,name="media_rec")
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

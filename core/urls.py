from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^config/$', views.config, name='config'),
    url(r'^images/$', views.get_all_media, name='images'),
    url(r'^images/(?P<filename>[0-9A-Za-z\.]{0,50})$', views.handle_delete_media_file, name='delete_image'),
    url(r'^incoming/$', views.handle_incoming_message, name='incoming'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

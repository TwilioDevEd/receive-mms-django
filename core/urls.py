from django.conf import settings
from django.urls import re_path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^config/$', views.config, name='config'),
    re_path(r'^images/$', views.get_all_media, name='images'),
    re_path(r'^incoming/$', views.handle_incoming_message, name='incoming'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

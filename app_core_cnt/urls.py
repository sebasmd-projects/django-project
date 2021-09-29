# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve


admin.autodiscover()

urlpatterns = []

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('apps.page.index.urls')),
    path('', include('apps.page.about.urls')),
    path('', include('apps.page.resume.urls')),
    path('', include('apps.page.blog.urls')),
    path('', include('apps.page.contact.urls')),
    path('', include('apps.general.users.urls')),
    path('', include('apps.nlp.nlp_admin.urls')),
    


    prefix_default_language=True

)

urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
] + staticfiles_urlpatterns() + urlpatterns
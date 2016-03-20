from django.conf import settings
from django.conf.urls import url

from dojango.util import media
from django.views import test, test_countries, test_states, datagrid_list

urlpatterns = [
    url(r'^test/$', test, name='dojango-test'),
    url(r'^test/countries/$', test_countries),
    url(r'^test/states/$', test_states),
    # Note: define accessible objects in DOJANGO_DATAGRID_ACCESS setting
    url(r'^datagrid-list/(?P<app_name>.+)/(?P<model_name>.+)/$', datagrid_list, name="dojango-datagrid-list"),
]

if settings.DEBUG:
    # serving the media files for dojango / dojo (js/css/...)
    urlpatterns += media.url_patterns

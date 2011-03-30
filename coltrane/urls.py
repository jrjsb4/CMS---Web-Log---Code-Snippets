from django.conf.urls.defaults import *

from coltrane.models import Entry

entry_info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'pub_date',
}

urlpatterns = patterns('django.views.generic.date_based',
    (r'^$', 'archive_index', entry_info_dict, 'coltrane_entry_archive_index'),
    (r'^(?P<year>\d{4})/$', 'object_detail', entry_info_dict, 'coltrane_entry_archive_year'), 
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/$', 'object_detail', entry_info_dict, 'coltrane_entry_archive_month'), 
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', 'object_detail', entry_info_dict, 'coltrane_entry_archive_day'), 
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'object_detail', entry_info_dict, 'coltrane_entry_detail'), 
)
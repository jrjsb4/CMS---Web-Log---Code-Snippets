from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#from coltrane.models import Entry

#entry_info_dict = {
#    'queryset': Entry.objects.all(),
#    'date_field': 'pub_date',
#}

urlpatterns = patterns('',
    # Example:
    # (r'^cms/', include('cms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # Search engine
    (r'^search/', 'cms.search.views.search'),
    
    # Coltrane weblog
    url(r'^weblog/', include('coltrane.urls')),
    
    # (r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 
    #    'coltrane.views.entry_detail'),

    # (r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 
    #    'django.views.generic.date_based.object_detail', entry_info_dict),
    
    # Tiny MCE WYSIWYG editor
    (r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve',
        { 'document_root': '/Users/jrb/Development/workspace/tinymce/jscripts/tiny_mce'}),
        
    # Include the flatpages urls
    (r'', include('django.contrib.flatpages.urls')),

)

from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from cms.search.models import SearchKeyword

class SearchKeywordInline(admin.StackedInline):
    model = SearchKeyword
    
class FlatPageAdminWithKeywords(FlatPageAdmin):
    inlines = [SearchKeywordInline]
    
# Calling unregister on an Model that isn't register results in an error, this must be new in v1.2.5 
admin.site.unregister(FlatPage)    
admin.site.register(FlatPage, FlatPageAdminWithKeywords)

# This is a simple registration class for the admin site; no longer used    
#class SearchKeywordAdmin(admin.ModelAdmin):
#    pass
#
# admin.site.register(SearchKeyword, SearchKeywordAdmin)

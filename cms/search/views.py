from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.shortcuts import render_to_response
from django.contrib.flatpages.models import FlatPage

# Create your views here.

# The following is the old search method that performs a query of flatpages
#from django.template import loader, Context
#def search(request):
#    query = request.GET['q']
#    results = FlatPage.objects.filter(content__icontains=query)
#    template = loader.get_template('search/search.html')
#    contetxt = Context({ 'query': query, 'results': results })
#    response = template.reder(context)
#    return HttpResponse(response)
        
def search(request):
    # return query from the submitted form, if no value set default value, empty string
    query = request.GET.get('q', '')
    keyword_results = results = []
    if query:
        keyword_results = FlatPage.objects.filter(searchkeyword__keyword__in=query.split()).distinct()
        if keyword_results.count() == 1:
            return HttpResponseRedirect(keyword_results[0].get_absolute_url())
        results = FlatPage.objects.filter(content__icontains=query)
    return render_to_response('search/search.html',
                              { 'query': query,
                                'keyword_results': keyword_results,
                                'results': results })
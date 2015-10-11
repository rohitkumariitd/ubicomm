from django.shortcuts import render
from django.views import generic
from ubic.models import UbicInstance
from django.db.models import Q
import datetime
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

class HomepageView(generic.ListView):
    template_name = 'homepage/main.html'
    context_object_name = 'ubic_list'

    def get_queryset(self):
    	queryParams = self.request.GET

    	searchQuery = queryParams.get('search')
    	sortBy = queryParams.get('sort')

    	ubicInstances = UbicInstance.objects.filter(
    			start_date__gte = datetime.datetime.now).order_by(
    			'start_date')
    	if searchQuery is not None:
	    	ubicInstances = ubicInstances.filter(
    			Q(ubic__name__icontains = searchQuery) | Q(ubic__description__icontains = searchQuery))
        if self.request.user.is_authenticated():
            print 'success' + self.request.user.email
    	return ubicInstances
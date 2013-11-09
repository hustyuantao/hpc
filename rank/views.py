from django.shortcuts import render
from rank.models import TopOneHundred

# Create your views here.
def top100list(request, nth):
	top100_list = TopOneHundred.objects.all().filter(nth=nth).order_by('rank')
	context = {'top100_list': top100_list}
	return render(request, 'rank/top100list.html', context)

def top500list(request, nth):
	top100_list = TopOneHundred.objects.all().filter(nth=nth).order_by('rank')
	context = {'top100_list': top100_list}
	return render(request, 'rank/top100list.html', context)
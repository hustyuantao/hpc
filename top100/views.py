from django.shortcuts import render
from top100.models import Ranking

# Create your views here.
def detail(request, nth):
	rankinglist = Ranking.objects.all().filter(nth=nth).order_by('rank')
	context = {'rankinglist': rankinglist}
	return render(request, 'top100/detail.html', context)

from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
	context_dictionary = {
		'first_name': 'guest'
	}
	return(render(request, 'homepage/index.html', context_dictionary))

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view1(request):
	s="Welcome to django"
	return HttpResponse(s)

def view2(request):
	m="Shashank"
	return HttpResponse(m)

def view3(request):
	s="<h1>This is 3rd Response"
	return HttpResponse(s)
	



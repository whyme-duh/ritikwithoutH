from typing import Generic
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView

from website.models import Blog, Education, Experience, Project, Service

context= {
	'projects' : Project.objects.all(),
	'educations' : Education.objects.all(),
	'services' : Service.objects.all(),
	'object' : Experience.objects.all(),
	'blogs' : Blog.objects.all()
}

def mainPage(request):
	return render(request , 'website/index.html', context)


class BlogDetailView(DetailView):
	model = Blog
	template_name = "website/blogdetail.html"
	





	

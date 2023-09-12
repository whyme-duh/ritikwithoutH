from typing import Generic
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView
from .forms import ContactForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from datetime import datetime

from website.models import Blog,  Skill, Project, Service, Bio

form = ContactForm()
context= {
		'projects' : Project.objects.all(),
		'services' : Service.objects.all(),
		'blogs' : Blog.objects.all(),
		'form': form,
		'files' :Bio.objects.all(),
		'date' : datetime.now().year,
		'skills' :Skill.objects.all
		# 'messages' : messages
	}
		

def mainPage(request):
	if request.method == "GET":
		form = ContactForm()
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			subject = form.cleaned_data['subject']

			try:
				send_mail(subject,name, email, ["ritikshrestha94@gmail.com"])
				messages.success(request, f"Sucessfull contacted. Wait for the response!")

			except BadHeaderError:
				return HttpResponse("Invalid Header Error")
        # return redirect("index")
		# 	form.save()
		# 	email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
		# 	email_message = form.cleaned_data['message']
		# 	if send_mail(email_subject, email_message, message_email, ['ritikshrestha94@gmail.com']):
		# 		messages.success(request, f"Sucessfull contacted. Wait for the response!")
		# 		return redirect('main-page')
		# 	else:
		# 		messages.error(request, f'Failed to send. Try Again!')
		# 		return redirect('main-page')
		# else:
		# 	form = ContactForm()
		
	return render(request , 'website/index2.html', context)

def developing_site(request):
	return render(request, 'website/developing.html')



def ProjectListView(request):
	project_list = Project.objects.all()
	paginator = Paginator(project_list, 5)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {
		'projects' : Project.objects.all(),
		'files' :Bio.objects.all(),
		'page_obj' : page_obj,
		'date' : datetime.now().year


	}
	return render(request, 'website/project_detail.html', context)

class BlogDetailView(DetailView):
	model = Blog
	template_name = "website/blogdetail.html"
	





	

from typing import Generic
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import DetailView
from .forms import ContactForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

from website.models import Blog, Contact, Education, Experience, Project, Service
form = ContactForm()
context= {
	'projects' : Project.objects.all(),
	'educations' : Education.objects.all(),
	'services' : Service.objects.all(),
	'object' : Experience.objects.all(),
	'blogs' : Blog.objects.all(),
	'form': form,
}

def mainPage(request):
	if request.method == "POST":
		form = ContactForm(request.POST)
		message_email = request.POST['email']
		if form.is_valid():
			form.save()
			email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
			email_message = form.cleaned_data['message']
			if send_mail(email_subject, email_message, message_email, ['ritikshrestha94@gmail.com']):
				messages.success(request, f"Sucessfull contacted. Wait for the response!")
				return redirect('main-page')
			else:
				messages.error(request, f'Failed to send. Try Again!')
				return redirect('main-page')
		else:
			form = ContactForm()
			
	return render(request , 'website/index.html', context)


class BlogDetailView(DetailView):
	model = Blog
	template_name = "website/blogdetail.html"
	





	

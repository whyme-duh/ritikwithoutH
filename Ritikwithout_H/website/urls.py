from django.urls import path
from Ritikwithout_H import settings
from django.conf.urls.static import static

from website.views import  BlogDetailView, mainPage, ProjectListView, developing_site, resourcePage

urlpatterns = [
	path('', mainPage, name ="main-page"),
    path('project/', ProjectListView, name ='project-detail'),
    path('resources/', resourcePage, name ='resources'),
	path('developing/',developing_site, name= "developing"),
	path('<slug:slug>/', BlogDetailView.as_view(), name= "blog-detail")

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
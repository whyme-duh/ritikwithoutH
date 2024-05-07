from distutils.command.upload import upload
from email.policy import default
from django.urls import reverse
from django.db import models
from PIL import Image
from ckeditor.fields import RichTextField
from django.core.validators import FileExtensionValidator

class Bio(models.Model):
	logo = models.ImageField(upload_to = "icons", null = True, blank= True)
	file = models.FileField(upload_to = "files")
	about_me_image = models.ImageField(upload_to="pictures", null = True, blank= True)
	front_image = models.ImageField(upload_to="pictures", null = True, blank= True)
	linkedin = models.URLField( null = True, blank= True)
	description = models.CharField(max_length=200, blank= True, null = True)
	github = models.URLField( null = True, blank= True)
	instagram = models.URLField( null = True, blank= True)
	pinterest = models.URLField( null = True, blank= True)

	def __str__(self):
		return "CV file : " + self.file.name

class Skill(models.Model):
	skill_name = models.CharField(max_length=80, null = False, blank=True)
	skill_image = models.ImageField(upload_to= "icons/skills" , null = True, blank= True)

	def __str__(self):
		return self.skill_name

class Project(models.Model):
	WEBSITE = "Website"
	MOBILEAPP = "MOBILE APP"
	ART = "ART"

	projects_categories = [
		(WEBSITE ,"Website" ),
		(MOBILEAPP , "MOBILE APP"),
		(ART, "ART"),
	]

	name = models.CharField(max_length=80)
	image = models.FileField(upload_to = "uploads/", null= True, blank = True, validators=[FileExtensionValidator(['jpeg','jpg', 'png', 'svg'])])
	content = models.TextField()
	source_code = models.URLField(null= True)
	view_link = models.URLField(null=True)
	category = models.CharField(max_length=80, choices=projects_categories, blank = False, null= True)

	def __str__(self) :
		return self.name

	def save(self, *args, **kwargs):
		super(Project, self).save(*args, **kwargs)
		img = Image.open(self.image.path)
		if img.height > 300 or img.width >400:
			output_size = (300, 400)
			img.thumbnail(output_size)
			img.save(self.image.path)


class Experience(models.Model):
	experience = models.CharField(max_length=70)
	time_interval = models.TextField(blank = False)
	content = models.TextField(blank= True)
	company = models.CharField(max_length=98, null= True, blank = False)
	link = models.URLField(null= True, blank =False)

	def __str__(self):
		return self.experience


	
class Education(models.Model):
	college = models.CharField(max_length=80)
	startingtime= models.CharField(max_length=10)
	endingtime= models.CharField(max_length=10)
	title= models.CharField(max_length=80)
	content = models.TextField(blank= True)

	def __str__(self):
		return self.college

class Service(models.Model):
	title = models.CharField(max_length=80)
	content = models.TextField()
	icon = models.CharField(max_length=100, blank = False, null = True)

	def __str__(self) :
		return self.title

	
class Blog(models.Model):
	title = models.CharField(max_length=80)
	author = models.CharField(max_length=50)
	# author_pic =models.ImageField(upload_to = "pictures/" , null = True, default= "images/pictures/mah.jpg")
	body= RichTextField(blank= False, null = False)
	image = models.ImageField(upload_to = "uploads/admin/", null = True)
	slug= models.SlugField(null = True, unique=True)
	blog_entry= models.CharField(max_length = 80, null = True,blank = False )
	created_at = models.DateField(auto_now_add=True, blank = False, null = True)

	def __str__(self) :
		return self.title

	def get_absolute_url(self):
		return reverse('blog-detail' ,kwargs = {'slug': self.slug})

	# def save(self, *args, **kwargs):
	# 	super(Blog, self).save(*args, **kwargs)
	# 	img = Image.open(self.author_pic.path)
	# 	if img.height > 100 or img.width >100:
	# 		output_size = (50, 50)
	# 		img.thumbnail(output_size)
	# 		img.save(self.author_pic.path)
	



from django.contrib import admin
from website.models import Blog, Education, Experience, Project, Service, Contact


admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Service)
admin.site.register(Contact)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
	list_display = ('title','author',)
	list_filter = ('title', )
	prepopulated_fields = {"slug": ("title",)}


from turtle import title
from django.contrib import admin
from .models import Project,ProjectFile,Partners
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    search_fields=['title','expiredDate']
    list_display=['title','budget','expired_date','goal','ongoing']
    list_display_links=list_display
    list_filter=('ongoing',)

class ProjectFileAdmin(admin.ModelAdmin):
    search_fields=['foreign_key__related_fieldname']

admin.site.register(Project,ProjectAdmin)
admin.site.register(ProjectFile,ProjectFileAdmin)
admin.site.register(Partners)
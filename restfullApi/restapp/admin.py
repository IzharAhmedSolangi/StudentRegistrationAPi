from django.contrib import admin
from .models import student , course ,enrolled

admin.site.register(student)
admin.site.register(course)

class adminEnrolled(admin.ModelAdmin):
    list_display = ['course','student' , 'total_amount_paid']
admin.site.register(enrolled,adminEnrolled)
# Register your models here.

from django.contrib import admin
from .models import myform


admin.site.register(myform)

class dformAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','subject','message')

# Register your models here.

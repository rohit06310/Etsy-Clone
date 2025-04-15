from django.contrib import admin # type: ignore
from .models import *

'''
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','image','description')'
    
'''

admin.site.register(Catagory)
admin.site.register(Product)
# Register your models here.

from django.contrib import admin
from .models import Phone

# Register your models here.
@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    # pass
    list_display = ('id', 'name', 'price', 'release_date', 'lte_exists') 
    list_filter = ('lte_exists', 'release_date')  
    #
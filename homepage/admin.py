from django.contrib import admin
from .models import Person
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    search_fields = ['last_name', 'first_name', 'first_meeting']
    list_filter = ('last_name', 'first_name', 'first_meeting')

admin.site.register(Person, PersonAdmin)



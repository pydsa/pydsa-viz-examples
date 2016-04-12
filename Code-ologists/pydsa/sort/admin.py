from django.contrib import admin
from sort.models import Sorting

# Register your models here.
class SortAdmin(admin.ModelAdmin):
    fields = ['Name','List']
    list_display = ('Name','List')


admin.site.register(Sorting, SortAdmin)

from django.contrib import admin
from .models import Todo
# Register your models here.

class TodAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')
    search_fields = ('title', 'description', 'completed')
    list_filter = ('title', 'description', 'completed',)
    list_editable = ( 'description', 'completed')

admin.site.register(Todo, TodAdmin)
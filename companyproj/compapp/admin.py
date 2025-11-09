from django.contrib import admin
from .models import Employee, Project
 
# Register your models here.
class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1
 
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'date_joined', 'phone_number')
    search_fields = ('name', 'position')
    list_filter = ('position', 'date_joined')
    inlines = [ProjectInline]
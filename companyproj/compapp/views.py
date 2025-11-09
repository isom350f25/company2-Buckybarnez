from django.shortcuts import render
from .models import Employee, Project

 
# Create your views here.
 
def employee_list(request):
    employees = Employee.objects.all().order_by('name')
    engineers = Employee.objects.filter(position__icontains='Engineer').order_by('name')
    return render(request, 'employee_list.html', {'employees': employees, 'engineers': engineers})
 
def employee_detail(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    projects = Project.objects.all()
    return render(request, 'employee_detail.html', {'employee':employee,'projects':projects})
 
def employee_engineers(request):
    engineers = Employee.objects.filter(position__icontains='Engineer')
    return render(request, 'employee_list.html', {'engineers': engineers})

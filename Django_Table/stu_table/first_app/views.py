from django.shortcuts import render
from .models import Student


# Create your views here.
def index(request):
    data=Student.objects.all()
    stu_count=data.count()
    stu_fname_with_m=data.filter(fname__startswith='M')
    return render(request,'students/index.html',{'record':data, #pass the all data as record
                                                 'stu_count': stu_count,  # Pass total student count
                                                  'stu_fname_with_m': stu_fname_with_m }) #pass students whose name sstarts with M


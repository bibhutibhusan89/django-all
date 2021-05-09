from django.shortcuts import render

# Create your views here.
from DjangoForm.models import StudentForm
from DjangoForm.forms import Student
from django.http import HttpResponse

def formRendering(request):
    student = StudentForm()
    return render(request,"index.html",{'form':student})

def formValidation(request):
    if request.method == "POST":
        form = Student(request.POST)
        if form.is_valid():
            try:
                return HttpResponse("Data Saved Successfully")
            except:
                pass
    else:
        form = Student()
    return render(request, 'index.html', {'form': form})


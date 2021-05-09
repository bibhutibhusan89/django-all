from django import forms
from DjangoForm.models import StudentForm

class Student(forms.ModelForm):
    class Meta:
        model = StudentForm
        fields = "__all__"
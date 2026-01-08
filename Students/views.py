from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

# Register Student
def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'Students/register.html', {'form': form})
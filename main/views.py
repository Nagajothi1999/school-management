from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from .decorator import role_required

# Create your views here.
@login_required(login_url='/login')
def home(request):
    if request.user.role == 'admin':
        return redirect('/admin-home')
    if request.user.role == 'staff':
        return redirect('/staff-home')
    if request.user.role == 'student':
        return redirect('/student-home')
    if request.user.role == 'editor':
        return redirect('/editor-home')
    return render(request,'main/home.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {"form": form})

@role_required(['admin'])
def admin_home(request):
    return render(request,'main/admin_home.html')

@role_required(['staff'])
def staff_home(request):
    return render(request,'main/staff_home.html')

@role_required(['student'])
def student_home(request):
    return render(request,'main/student_home.html')

@role_required(['editor'])
def editor_home(request):
    return render(request,'main/editor_home.html')

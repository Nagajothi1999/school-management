from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def home(request):
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


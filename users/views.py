from multiprocessing import context
from django.shortcuts import redirect, render , render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .forms import SingUpForm , UserUpdateForm , ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def sing_up(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SingUpForm()
    context ={
        'form':form
    }
    return render(request,'users/singup.html',context)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST or None , instance = request.user)
        p_form = ProfileUpdateForm(request.POST or None , request.FILES or None, instance = request.user.profilemodel)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('user-profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profilemodel)
        
    context = {
        'u_form': u_form,
        'p_form':p_form
        
    }
    return render(request,'users/profile.html',context)
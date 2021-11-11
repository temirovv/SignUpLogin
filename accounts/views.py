from django.shortcuts import render
from .forms import CustomUserForm
from django.shortcuts import redirect
from django.contrib.auth import login as auth_login


def signup(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('login')
    else:
        form = CustomUserForm()
    return render(request, 'signup.html', {'form': form})

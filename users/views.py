from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from users.forms import UserRegisterForm
from django.contrib.auth import authenticate,login,logout
def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/login')
    else:
        form = UserRegisterForm()
    return render(request,"register.html",{'form':form})
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("/chat/1")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request,"login.html",{"form": form})
def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("login")


def profile(request, username: str = ""):
    if not username:
        return redirect('home')
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('home')
    return render(request, 'profile.html',
                  {
                    'profile':user.profile,
                    'username':user.username
                  }
                  )
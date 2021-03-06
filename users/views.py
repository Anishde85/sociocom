from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from users.forms import UserRegisterForm
from django.contrib.auth import authenticate,login,logout
from recommendation import get_recommendations

def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username exists.")
                return redirect('/register')
            form.save()
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
                return redirect("/room")
            else:
                messages.info(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request,"login.html",{"form": form})
def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("landing")

def recommendations(request):
    if not request.user.is_authenticated:
        return redirect('home')
    username = request.user.username
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('landing')
    recs = []
    for name, categories, price, image, link in get_recommendations(user.profile.messages):
        if len(price)==0:
            price="NA"
        recs += [{'link': link, 'image': image, 'name': name, 'categories': categories, 'price': price}]
    return render(request, 'recommendations.html',
                  {
                      'username': user.username,
                      'recs': recs
                  }
                  )

def profile(request, username: str = ""):
    if not username and not request.user.is_authenticated:
        return redirect('login')
    elif not username:
        username = request.user.username
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('login')
    return render(request, 'profile.html',
                  {
                    'profile':user.profile,
                    'username':user.username
                  }
                  )
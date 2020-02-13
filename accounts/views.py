from django.shortcuts import render, redirect
# 로그인 필수요건!
from django.contrib.auth.models import User

from django.contrib import auth

 

# Create your views here.


def signup(request):
    if request.method == 'POST':
        if request.POST["password1"] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST["username"], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('home')
        return render(request, 'signup.html')

    return render(request, 'signup.html')


def login(request):
    #POST 방식으로 들어오면
    if request.method == 'POST':
        #username/password에 각각 넘겨받은거 저장
        username = request.POST['username']
        password = request.POST['password']
        #우리 서버에 회원이 맞아요?
        user =auth.authenticate(request, username=username, password=password)
        #우리 user맞아요!
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        #우리 user아닌뎅?
        else:
            return render(request, 'login.html', {'error':'username or password is incorrect.'})
    else:
        return render(request,'login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')
    else:
        return render(request,'login.html')


from django.shortcuts import redirect, render
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth import authenticate
from account.models import MyUser
from django.contrib.auth.hashers import check_password

# Create your views here.


def login(request):
    return render(request, 'account/login.html')


def logincheck(request):
    if request.method == 'POST':
        print("request"+str(request))
        print("body"+str(request.body))
        userid = request.POST.get('userid', '')
        userpassword = request.POST.get('userpw', '')
        if not (userid and userpassword):
            print("아이디와 비밀번호를 모두 입력하세요.")
        else:
            myuser = MyUser.objects.get(user_id=userid)
            if (userpassword == myuser.password):
                request.session['user'] = myuser.user_id
                return redirect('mainpage')
            else:
                print("비밀번호가 맞지않습니다.")
                return redirect('login')


def signup(request):
    return render(request, 'account/signup.html')


def signupcheck(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password1 = request.POST.get('password1', None)
        password2 = request.POST.get('password2', None)
        mes_data = {}
        if not (username and password1 and password2):
            mes_data['error'] = "모든값을 입력하세요."
        if password1 != password2:
            mes_data['error'] = "비밀번호가 다릅니다."
        else:
            user = MyUser(user_name=username, password=password1)
            user.save()
            print("request"+str(request))
            print("request body :" + str(request.body))
            return render(request, 'account/login.html', mes_data)


def logout(request):
    request.session.pop('user')
    return redirect('mainpage')

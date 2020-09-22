from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import User


# Create your views here.
def login(request):
    if request.method == 'GET':
        print('login get')
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        res_data = dict()
        if not (username and password):
            res_data['error'] = '빈 입력 값이 있습니다.'
        else:
            user = User.objects.get(username=username)
            print(user)
            if check_password(password, user.password):
                pass
            else :
                res_data['error'] = '비밀번호가 틀렸습니다.'


        return render(request, 'login.html', res_data)


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = dict()

        if not(username and useremail and password and re_password):
            res_data['error'] = '빈 입력 값이 있습니다.'
        if password != re_password:
            res_data['error'] = '비밀번호가 일치하지 않습니다.'
        else:
            user = User(
                username=username,
                useremail=useremail,
                password=make_password(password),
            )
            user.save()

        return render(request, 'register.html', res_data)






from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

import json
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def login(request: HttpRequest):
    user_data = {
        'username': 'python',
        'password': 'django'
    }

    context = {
        'method': request.method,
        'is_valid': True
    }

    if request.method == 'GET':
        return render(request, 'users/login.html', context)

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # 유저가 아이디나 비밀번호를 입력하는 상황에서 실수롤 정보를 다 기입하지 않은 상황
        if username == '':
            context['is_valid'] = False
        if password == '':
            context['is_valid'] = False

        if username != user_data['username']:
            context['is_valid'] = False
        if password != user_data['password']:
            context['is_valid'] = False
        
        if context['is_valid']:
            responce = redirect('pages:index')
            
            responce.set_cookie('username', user_data['username'])
            responce.set_cookie('password', user_data['password'])
            responce.set_cookie('is_login', True)
            
            return responce

        return render(request, 'users/login.html', context)


def login_detail(request: HttpRequest, id):
    return HttpResponse(f"user id는 {id}입니다.")

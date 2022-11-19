from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

import json
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def login(request: HttpRequest):
    user_data = {
        'username': 'python',
        'password': 'django'
    }

    if request.method == 'GET':
        return render(request, 'users/login.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # 유저가 아이디나 비밀번호를 입력하는 상황에서 실수롤 정보를 다 기입하지 않은 상황
        if username == '':
            return HttpResponse('유저 아이디를 입력해주세요')
        if password == '':
            return HttpResponse('유저 비밀번호를 입력해주세요')

        if username != user_data['username']:
            return HttpResponse('유저 아이디가 올바르지 않습니다.')
        if password != user_data['password']:
            return HttpResponse('유저 비밀번호가 올바르지 않습니다.')
        
        return HttpResponse('로그인 성공!')

    

def login_detail(request: HttpRequest, id):
    return HttpResponse(f"user id는 {id}입니다.")
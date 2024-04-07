from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Task  # 모델 임포트
from django.core.serializers import serialize
import json

# Create your views here.


def home_view(request, username=None):
    if username:
        user = get_object_or_404(User, username=username)
    else:
        # username이 URL에 제공되지 않았다면 현재 로그인된 사용자를 사용합니다.
        user = request.user
        if not request.user.is_authenticated:
            # 사용자가 로그인하지 않았다면 로그인 페이지로 리다이렉트합니다.
            return redirect("account_login")

    tasks = Task.objects.filter(user=user)
    tasks_json = serialize("json", tasks)  # 데이터를 JSON 형식으로 변환

    return render(
        request, "a_home/home.html", {"profile": user.profile, "tasks": tasks_json}
    )

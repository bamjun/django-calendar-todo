from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Task  # 모델 임포트
from django.core.serializers import serialize

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.dateparse import parse_datetime

# @login_required
# def home_view(request, username=None):
#     if username:
#         user = get_object_or_404(User, username=username)
#     else:
#         # username이 URL에 제공되지 않았다면 현재 로그인된 사용자를 사용합니다.
#         user = request.user
#         if not request.user.is_authenticated:
#             # 사용자가 로그인하지 않았다면 로그인 페이지로 리다이렉트합니다.
#             return redirect("account_login")

#     tasks = Task.objects.filter(user=user)
#     tasks_json = serialize("json", tasks)  # 데이터를 JSON 형식으로 변환

#     return render(
#         request, "a_home/home.html", {"profile": user.profile, "tasks": tasks_json}
#     )




@login_required
def home_view(request, username=None):
    if request.method == "POST":
        title = request.POST.get("title")
        start_date = parse_datetime(request.POST.get("start_date"))
        end_date = parse_datetime(request.POST.get("end_date"))
        status = request.POST.get("status")
        
        # 새 Task 객체 생성 및 저장
        new_task = Task(
            user=request.user,
            title=title,
            start_date=start_date,
            end_date=end_date,
            status=status,
        )
        new_task.save()
        
        # 작업 저장 후 현재 페이지로 리디렉션
        return HttpResponseRedirect(reverse('home'))

    # 기존 home_view 코드
    if username:
        user = get_object_or_404(User, username=username)
    else:
        user = request.user
        if not request.user.is_authenticated:
            return redirect("account_login")

    tasks = Task.objects.filter(user=user)
    tasks_json = serialize("json", tasks)

    return render(request, "a_home/home.html", {"profile": user.profile, "tasks": tasks_json})
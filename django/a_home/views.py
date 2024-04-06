from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
# Create your views here.


def home_view(request, username=None):
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        try:
            profile = request.user.profile
        except:
            return redirect('account_login')
    return render(request, 'a_home/home.html', {'profile': profile})
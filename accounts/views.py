import json
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
# from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, render_to_response
from django.views.decorators.http import require_POST

from django.contrib.auth import logout as django_logout
# from django.contrib.auth.views import LoginView
#
#
# from allauth.socialaccount.models import SocialApp
# from allauth.socialaccount.templatetags.socialaccount import get_providers
from .forms import SignupForm, ProfileForm, LoginForm
from .models import Profile, Relation



def login_check(request):
    if request.method == "POST":
        #사용자가 로그인 폼에 입력한 값
        form = LoginForm(request.POST)
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        #인증
        user = authenticate(username=name, password=pwd)
        if user is not None: # 로그인 성공
            login(request, user)
            return redirect("/")
        else: #로그인 실패
            return render(request, 'accounts/login_fail_info.html')
    else: #get 방식인 경우 - 로그인 페이지로 이동
        form = LoginForm()
        return render(request, 'accounts/login.html', {"form":form})


    # if request.method == 'POST':
    #     # 로그인 성공 후 이동할 URL. 주어지지 않으면 None
    #     next = request.GET.get('next')
    #
    #     # Data bounded form인스턴스 생성
    #     # AuthenticationForm의 첫 번째 인수는 해당 request가 되어야 한다
    #     login_form = LoginForm(request=request, data=request.POST)
    #
    #     # 유효성 검증에 성공할 경우
    #     # AuthenticationForm을 사용하면 authenticate과정까지 완료되어야 유효성 검증을 통과한다
    #     if login_form.is_valid():
    #         # AuthenticatonForm에서 인증(authenticate)에 성공한 유저를 가져오려면 이 메서드를 사용한다
    #         user = login_form.get_user()
    #         # Django의 auth앱에서 제공하는 login함수를 실행해 앞으로의 요청/응답에 세션을 유지한다
    #         django_login(request, user)
    #         # next가 존재하면 해당 위치로, 없으면 Post목록 화면으로 이동
    #         return redirect(next if next else 'post:post_list')
    #     # 인증에 실패하면 login_form에 non_field_error를 추가한다
    #     login_form.add_error(None, '아이디 또는 비밀번호가 올바르지 않습니다')
    # else:
    #     login_form = LoginForm()
    #
    # context = {
    #     'login_form': login_form,
    # }
    #
    #
    # providers = []
    # for provider in get_providers():  # settings/INSTALLED_APPS 내에서 활성화된 목록
    #     # social_app속성은 provider에는 없는 속성입니다.
    #     try:
    #         # 실제 provider 별 Client id/secret 이 등록이 되어 있는가?
    #         provider.social_app = SocialApp.objects.get(provider=provider.id, sites=settings.SITE_ID)
    #     except SocialApp.DoesNotExist:
    #         provider.social_app = None
    #     providers.append(provider)
    # return render(request, 'accounts/login.html', {'providers': providers}, context)


def logout(request):
    django_logout(request)
    return redirect("/")


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():  # clean_<필드명> 메소드 호출
            user = form.save()
            return redirect('accounts:login')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })


@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, '비밀번호가 정상적으로 변경되었습니다.')
            return redirect('post:my_post_list', request.user.username)
        else:
            messages.error(request, '오류가 발생하였습니다.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/password_change.html', {
        'form': form,
    })


@login_required
def account_change(request):
    profile = get_object_or_404(Profile, pk=request.user.profile.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save()
            messages.success(request, '회원정보가 정상적으로 변경되었습니다.')
            return redirect('post:my_post_list', request.user.username)
        else:
            messages.error(request, '오류가 발생하였습니다.')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/account_change.html', {
        'form': form,
    })


@login_required
@require_POST
def follow(request):
    from_user = request.user.profile
    pk = request.POST.get('pk')
    to_user = get_object_or_404(Profile, pk=pk)
    relation, created = Relation.objects.get_or_create(from_user=from_user, to_user=to_user)

    if created:
        message = '팔로우 시작!'
        status = 1
    else:
        relation.delete()
        message = '팔로우 취소'
        status = 0

    context = {
        'message': message,
        'status': status,
    }
    return HttpResponse(json.dumps(context), content_type="application/json")
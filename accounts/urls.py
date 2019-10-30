from django.urls import path
from .views import *


app_name = 'accounts'

urlpatterns = [
    path('login/', login_check, name='login'),
    # path('logout/', auth_views.logoutas_view(), name='logout', kwargs={'next_page': 'login'}),
    path('logout/', logout, name='logout'),
    path('signup/', signup, name='signup'),
    path('password_change/', password_change, name='password_change'),
    path('account_change/', account_change, name='account_change'),
    path('follow/', follow, name='follow'),



    # url(r'^login/$', views.login, name='login'),
    # url(r'^login/$', auth_views.login, name='login', kwargs={'template_name': 'accounts/login.html'}),

    # url(r'^logout/$', auth_views.logout, name='logout', kwargs={'next_page': 'login'}),
    # url(r'^signup/$', views.signup, name='signup'),
    # url(r'^password_change/$', views.password_change, name='password_change'),
    # url(r'^account_change/$', views.account_change, name='account_change'),
    # url(r'^follow/$', views.follow, name='follow'),
]

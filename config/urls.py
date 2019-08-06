"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('post/', include('post.urls', namespace='post')),
    path('', lambda r: redirect('post:post_list'), name='root'),
]

# NOTE: serving media files uploaded by a user during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# NOTE: debug_toolbar용 url 설정
# if settings.DEBUG:
#     import debug_toolbar
#
#     urlpatterns += [
#         url(r'^__debug__/', include(debug_toolbar.urls)),
#     ]

"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from utils.swagger import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/article/", include("article.routers")),
    path("api/user/", include("user.routers")),
    path("api/book/", include("book.routers")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # 登陆
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # 刷新令牌
]

if settings.DEBUG:  # 开发环境下
    urlpatterns += [
        re_path(
            r"swagger/$",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui"
        )
    ]

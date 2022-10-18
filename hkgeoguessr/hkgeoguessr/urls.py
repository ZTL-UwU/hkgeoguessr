"""hkgeoguessr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from problem.views import (ProblemView, ProblemAnswerView)

from account.views import (
    AccountView,
)

urlpatterns = [
    # Problem
    path('api/problem/<int:pid>', ProblemView.as_view()),
    path('api/problem', ProblemView.as_view()),
    path('api/problem/ans/<int:pid>', ProblemAnswerView.as_view()),

    # Account
    path('api/account', AccountView.as_view()),
    path('api/account/<int:uid>', AccountView.as_view()),

    # Admin
    path('admin/', admin.site.urls),
]

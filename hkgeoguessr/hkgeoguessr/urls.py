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

from money.views import (MoneyView, MoneyAnswerView)
from place.views import (PlaceView, PlaceAnswerView)

from account.views import (
    AccountView,
    AccountSessionView
)

urlpatterns = [
    # Money problem
    path('api/money/<int:pid>', MoneyView.as_view()),
    path('api/money', MoneyView.as_view()),
    path('api/money/ans/<int:pid>', MoneyAnswerView.as_view()),

    # Place problem
    path('api/place/<int:pid>', PlaceView.as_view()),
    path('api/place', PlaceView.as_view()),
    path('api/place/ans/<int:pid>', PlaceAnswerView.as_view()),

    # Account
    path('api/account', AccountView.as_view()),
    path('api/account/<int:uid>', AccountView.as_view()),
    path('api/account/session', AccountSessionView.as_view()),

    # Admin
    path('admin/', admin.site.urls),
]

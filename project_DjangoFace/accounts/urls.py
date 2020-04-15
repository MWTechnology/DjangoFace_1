from django.contrib.auth import views
from django.urls import path, include
from django.conf.urls import url
from . import views as s
from account.views import (
    PasswordResetTokenView,
    PasswordResetView,
)

from django.contrib.auth import views as authViews




urlpatterns = [
    path('login/', s.MyLoginView.as_view(), name='login'),

    path('exit/', authViews.LogoutView.as_view(next_page='login'), name='exit'),

    path('password-change/', s.MyPasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('register/', s.MyRegisterFormView.as_view(), name="register"),
    path('register_sent/', s.register_sent, name="register_sent"),

    path('password-reset/', s.MyPasswordResetView.as_view(), name="account_password_reset"),
    path('reset/<uidb36>/<token>/', PasswordResetTokenView.as_view(), name='account_password_reset_token'),





    path ('someview/', s.someview, name='someview'),

]


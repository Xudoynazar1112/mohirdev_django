from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView,\
    PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView
from django.urls import path
from .views import *

urlpatterns = [
    # path('login/', user_login, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_coniform'),
    path('password-reset/complate/', PasswordResetCompleteView.as_view(), name='password_reset_complate'),
    path('profile/', dashboard_view, name='user_profile'),
    path('signup/', user_registr, name='user_registr'),
    # path('signup/', SignUpView.as_view(), name='user_registr'),
    # path('profile/edit/', edit_user, name='edit_user_informations'),
    path('profile/edit/', EditUserView.as_view(), name='edit_user_informations'),

]


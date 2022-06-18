from django.urls import path
from user_pro import views
from django.contrib.auth import views as auth_views # for login and logout

urlpatterns = [
    path('register',views.user_register,name='register'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('login',views.user_login,name='login'),
    path('logout',views.user_logout,name='logout'),
    path("profile/<int:user_id>", views.user_profile, name='profile'),

    ##reset password########
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    ########################
    
]
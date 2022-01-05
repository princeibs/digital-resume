from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'resume'

urlpatterns= [
    path('', views.IndexView.as_view(), name='index'),
    path('password-reset/', views.ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name='resume/user/password_reset_confirm.html'), 
        name='password_reset_confirm'),
    path('password-reset-complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name='resume/user/password_reset_complete.html'),
        name='password_reset_complete'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolios'),
    path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name='portfolio'),
    path('blog/', views.BlogView.as_view(), name='blogs'),
    path('blog/<slug:slug>', views.BlogDetailView.as_view(), name='blog')
] 
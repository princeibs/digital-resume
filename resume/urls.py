from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'resume'

urlpatterns= [
    path('', views.IndexView.as_view(), name='index'),
    path('password-reset/', views.ResetPasswordView.as_view(), name='password_reset'),    
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolios'),
    path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name='portfolio'),
    path('blog/', views.BlogView.as_view(), name='blogs'),
    path('blog/<slug:slug>', views.BlogDetailView.as_view(), name='blog')
] 
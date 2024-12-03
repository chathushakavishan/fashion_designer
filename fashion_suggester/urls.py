from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user-feedback/', views.dashboard, name='user-feedback'),
    path('feedback-suggestion/', views.feedback_suggestion, name='feedback-suggestion'),
    path('redirect/', views.redirect_to_dashboard, name='redirect-to-dashboard'),
    
]

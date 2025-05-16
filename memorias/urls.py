from django.urls import path
from . import views

app_name = 'memorias'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('chatBot/', views.chatBot_view, name='chatBot'),
]
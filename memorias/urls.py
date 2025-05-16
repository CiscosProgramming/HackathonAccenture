from django.urls import path
from . import views

urlpatterns = [
    path('chatBot/', views.chatBot_view, name='chatbot'),
]
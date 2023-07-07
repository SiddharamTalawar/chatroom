from django.urls import path

from .views import UserRegisterView,room

urlpatterns = [
    path('', UserRegisterView.as_view(), name='index'),
    path('<str:room_name>/', room, name='room'),
]
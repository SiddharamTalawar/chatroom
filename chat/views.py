from django.shortcuts import render
from django.views.generic import CreateView

from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


class UserRegisterView(CreateView):
	form_class = UserCreationForm
	template_name = 'register.html'
	success_url = reverse_lazy('login')

@login_required(login_url='registration/login', redirect_field_name='index')
def rooom(request, room_name):
    print('~~~DEBUG~~~')
    return render(request, 'chatroom.html', {
        'room_name': room_name
    })

def room(request, room_name):
    print('~~~DEBUG~~~')
    return render(request, 'chatroom.html', {
        'room_name': room_name
    })
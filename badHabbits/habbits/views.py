from django.shortcuts import render
from .models import User

def index(request):
    users = User.objects.order_by('-name')[:10]
    context = {'users': users}
    return render(request, 'habbits/index.html', context)

def detail(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'habbits/detail.html', {'user': user})

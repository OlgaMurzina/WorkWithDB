from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name') # получить значение поля Имя
        age = request.POST.get('age') # получить значение поля Возраст
        return HttpResponse(f'<h2>Привет, {name}, твой возраст: {age}</h2>')
    else:
        userform = UserForm()
        return render(request, 'index.html', {'form': userform})
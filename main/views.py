from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def show_subscribe(request):
    return render(request, 'subscribe.html', {})


#ajax handle code


def save_subscribe(request):
    if request.method == "GET":
        print(request.GET.get('email'))
    return JsonResponse({'subscribed': True})

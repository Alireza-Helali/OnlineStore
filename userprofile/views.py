from django.shortcuts import render
from django.views import View
from .forms import RegisterForm


# Create your views here.

class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register_page.html', context={'form': form})

from audioop import reverse

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import ProfileForm, ProfileExtraForm


class Registration(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'

    def get(self, request, *args):
        return render(request, self.template_name, {'form': ProfileForm, 'form2': ProfileExtraForm})

    def post(self, request, **kwargs):
        form = ProfileForm(request.POST)
        form2 = ProfileExtraForm(request.POST)
        if all((form.is_valid(), form2.is_valid())):
            user = form.save()
            values = form2.save(commit=False)
            values.fKey = user
            values.save()

        print(request.POST)

        return redirect('login')

    def login(request):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('home'))
        else:
            return LoginView.as_view(authentication_form=ProfileForm)(request)

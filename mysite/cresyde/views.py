from audioop import reverse

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import ProfileForm, ProfileExtraForm, LoginForm


class Registration(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

    def get(self, request, *args):
        return render(request, self.template_name, {'form': ProfileForm, 'form2': ProfileExtraForm})

    def post(self, request):
        form = ProfileForm(request.POST)
        form2 = ProfileExtraForm(request.POST)

        if form.is_valid():
            form.save()

            if form2.is_valid():
                form2.save()

        return redirect('home')

    def login_page(request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            username = username.lower()
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            if user.is_staff:
                return redirect('sweet:vendor_index')
            else:
                return redirect('sweet:index')
        else:
            errors = "Invalid Username or Password"


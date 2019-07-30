from audioop import reverse

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import ProfileForm


class Registration(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

    def get(self, request, *args):
        return render(request, self.template_name, {'form': Registration,'form2': ProfileForm})


    def post(self, request):
        form = ProfileForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('home')


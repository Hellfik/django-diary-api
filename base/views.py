from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib import messages

from rest_framework import viewsets
from rest_framework import permissions

from crispy_forms.layout import Submit

from django.urls import reverse_lazy


from .models import Text

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def homePage(request):
    return render(request, 'base/home.html')



class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    success_message = "Bienvenue sur l'application, nous sommes heureux de vous revoir"

    def get_success_url(self) -> str:
        return reverse_lazy('texts')



class RegisterView(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('texts')
    success_message = "Bienvenue sur l'application, nous sommes heureux de vous voir parmis nous"

    class Model:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form), self.success_message

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            messages.success(self.request, self.success_message)
            return redirect('texts')
        return super(RegisterView,self).get(*args, **kwargs)


# Create your views here.
class TextList(LoginRequiredMixin,ListView):
    model = Text
    context_object_name = 'texts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['texts'] = context['texts'].filter(client=self.request.user)

        search_input = self.request.GET.get('search') or ''
        if search_input:
            context['texts'] = context['texts'].filter(text__contains=search_input)
        
        context['search'] = search_input
        return context


class TextDetail(LoginRequiredMixin ,DetailView):
    model = Text
    context_object_name = 'text'
    # If we want to rename the template base used by default
    #template_name = 'base/task.html'

class TextCreate(LoginRequiredMixin,CreateView):
    model = Text
    # List all fields of the Text class
    fields = ['text']
    success_url = reverse_lazy('texts')
    success_message = "Votre texte a bien été créé !!!"

    def form_valid(self, form):
        form.instance.client = self.request.user
        return super(TextCreate,self).form_valid(form)


class TextUpdate(LoginRequiredMixin,UpdateView):
    model = Text
    fields = '__all__'
    success_url = reverse_lazy('texts')
    success_message = "Votre texte a bien été modifié !!!"


class TextDelete(LoginRequiredMixin,DeleteView):
    model = Text
    context_object_name = 'text'
    success_url = reverse_lazy('texts')
    success_message = "Votre texte a bien été supprimé !!!"




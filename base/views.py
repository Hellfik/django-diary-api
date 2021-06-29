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
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator

import pickle


def homePage(request):
    return render(request, 'base/home.html')

def profilePage(request):
    current_user = request.user
    texts = Text.objects.filter(client=current_user.id).count()
    texts_happy = Text.objects.filter(client=current_user.id, emotion="happy").count()
    texts_sadness = Text.objects.filter(client=current_user.id, emotion="sadness").count()
    texts_anger = Text.objects.filter(client=current_user.id, emotion="anger").count()
    texts_fear = Text.objects.filter(client=current_user.id, emotion="fear").count()
    texts_love = Text.objects.filter(client=current_user.id, emotion="love").count()
    texts_surprise = Text.objects.filter(client=current_user.id, emotion="surprise").count()
    per_cent_happy = round((texts_happy/texts),2) * 100
    per_cent_sadness = round((texts_sadness/texts),2) * 100
    per_cent_anger = round((texts_anger/texts),2) * 100
    per_cent_fear = round((texts_fear/texts),2) * 100
    per_cent_love = round((texts_love/texts),2) * 100
    per_cent_surprise = round((texts_surprise/texts),2) * 100
    #texts2 = Text.objects.filter(emotion="happy").count()
    context = {
        "texts": texts,
        "texts_happy": texts_happy,
        "texts_sadness": texts_sadness,
        "texts_anger": texts_anger,
        "texts_fear": texts_fear,
        "texts_love": texts_love,
        "texts_surprise": texts_surprise,
        "per_cent_happy": per_cent_happy,
        "per_cent_sadness": per_cent_sadness,
        "per_cent_anger": per_cent_anger,
        "per_cent_fear": per_cent_fear,
        "per_cent_love": per_cent_love,
        "per_cent_surprise": per_cent_surprise,
    }
    return render(request, 'base/profile.html', context)

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
        fields = ('username', 'password1', 'password2')


    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            messages.success(self.request, self.success_message)
            return redirect('texts')
        return super(RegisterView,self).get(*args, **kwargs)


# Create your views here.
class TextList(LoginRequiredMixin,ListView):
    model = Text
    context_object_name = 'texts'
    #paginate_by = 10

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
        tfidf, model = pickle.load(open('./dl-model/lr_combined_tfidf.bin', 'rb'))
        y_pred = model.predict(tfidf.transform([form.instance.text]))
        form.instance.emotion = y_pred[0]
        return super(TextCreate,self).form_valid(form)


class TextUpdate(LoginRequiredMixin,UpdateView):
    model = Text
    fields = ['text']
    success_url = reverse_lazy('texts')
    success_message = "Votre texte a bien été modifié !!!"

    def form_valid(self, form):
        tfidf, model = pickle.load(open('./dl-model/lr_combined_tfidf.bin', 'rb'))
        y_pred = model.predict(tfidf.transform([form.instance.text]))
        form.instance.emotion = y_pred[0]
        return super(TextUpdate,self).form_valid(form)

class TextDelete(LoginRequiredMixin,DeleteView):
    model = Text
    context_object_name = 'text'
    success_url = reverse_lazy('texts')
    success_message = "Votre texte a bien été supprimé !!!"




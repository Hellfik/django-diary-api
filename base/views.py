from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib import messages

from rest_framework import viewsets
from rest_framework import permissions

from django.urls import reverse_lazy


from .models import Text

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator

from django.http import HttpResponse
from rest_framework import status

import pickle


def homePage(request):
    """
    Display the home page of the application

    **parameters**
    request => Any request that can be made in the view

    **return**
    Return the associated view with the render function
    """
    return render(request, 'base/home.html')

def profilePage(request):
    """
    Display the profile of the current logged in user. It shows informations as well as his own emotion weel

    **parameter**
    request => Any request that can be made in the view

    **return**
    Return the associated view with the render function
    """
    # Get the current logged in user
    current_user = request.user
    # Get the number of texts associated with this user
    try:
        texts = Text.objects.filter(client=current_user.id).count()
    except Text.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    # Get the number of texts associated with each emotion: Will be used to create the emotion weel
    texts_happy = Text.objects.filter(client=current_user.id, emotion="happy").count()
    texts_sadness = Text.objects.filter(client=current_user.id, emotion="sadness").count()
    texts_anger = Text.objects.filter(client=current_user.id, emotion="anger").count()
    texts_fear = Text.objects.filter(client=current_user.id, emotion="fear").count()
    texts_love = Text.objects.filter(client=current_user.id, emotion="love").count()
    texts_surprise = Text.objects.filter(client=current_user.id, emotion="surprise").count()
    # Translation in percentage
    per_cent_happy = round((texts_happy/texts),2) * 100
    per_cent_sadness = round((texts_sadness/texts),2) * 100
    per_cent_anger = round((texts_anger/texts),2) * 100
    per_cent_fear = round((texts_fear/texts),2) * 100
    per_cent_love = round((texts_love/texts),2) * 100
    per_cent_surprise = round((texts_surprise/texts),2) * 100
    # The context is need to retrieve data in the template
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
    """
    Creates of custom login view : if the user successfully logged in it will redirect him
    """
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    success_message = "Bienvenue sur l'application, nous sommes heureux de vous revoir"

    def get_success_url(self) -> str:
        return reverse_lazy('texts')



class RegisterView(FormView):
    """
    Creates of view with a registration form : New users will be able to create a new account by filling in the form
    After registration, they will be logged in by default and have acces to their account
    """
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('texts')
    success_message = "Bienvenue sur l'application, nous sommes heureux de vous voir parmis nous"

    class Model:
        model = User
        fields = ('username', 'password1', 'password2')


    def form_valid(self, form):
        """
        Check if the form is valid before creating the user
        """
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
    """
    Creates the view that list all of the user's texts : It requires to be authenticated
    """
    model = Text
    context_object_name = 'texts'
    #paginate_by = 10

    def get_context_data(self, **kwargs):
        """
        Get all texts associated to the user and display them
        **return**
        Return the context (a list of all the data we want to display on the template)
        """
        context = super().get_context_data(**kwargs)
        context['texts'] = context['texts'].filter(client=self.request.user)

        # Search functionality
        search_input = self.request.GET.get('search') or ''
        if search_input:
            context['texts'] = context['texts'].filter(text__contains=search_input)
        
        context['search'] = search_input
        return context

#########################
#         CRUD          #
#########################

class TextDetail(LoginRequiredMixin ,DetailView):
    """
    Show the text informations
    """
    model = Text
    context_object_name = 'text'

class TextCreate(LoginRequiredMixin,CreateView):
    """
    Creates a view where a logged user can submit his daily text, the emotion will be predicted with the help of a machine learning model
    """
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
    """
    Creates a view where a logged user can modify his own texts
    """
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
    """
    Creates a view where a logged user can delete his own text
    """
    model = Text
    context_object_name = 'text'
    success_url = reverse_lazy('texts')
    success_message = "Votre texte a bien été supprimé !!!"




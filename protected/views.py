from base.models import Text
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser

# Create your views here.


class CustomLoginView(LoginView):
    """
    Creates of custom login view : if the user successfully logged in it will redirect him
    """
    template_name = 'protected/login_admin.html'
    fields = '__all__'
    redirect_authenticated_user = True
    success_message = "A bientot"

    def get_success_url(self) -> str:
        return reverse_lazy('protected_admin')



@staff_member_required(login_url='login')
def protectedView(request):

    # Get models infos to display
    texts_count = Text.objects.all().count()
    users_count = User.objects.all().count()
    users = User.objects.all()
    

    # Get all the data needed for the global emotion weel
    # Get the number of texts associated with each emotion: Will be used to create the emotion weel
    texts_happy = Text.objects.filter(emotion="happy").count()
    texts_sadness = Text.objects.filter(emotion="sadness").count()
    texts_anger = Text.objects.filter(emotion="anger").count()
    texts_fear = Text.objects.filter(emotion="fear").count()
    texts_love = Text.objects.filter(emotion="love").count()
    texts_surprise = Text.objects.filter(emotion="surprise").count()

     # Translation in percentage
    per_cent_happy = round((texts_happy/texts_count),2) * 100
    per_cent_sadness = round((texts_sadness/texts_count),2) * 100
    per_cent_anger = round((texts_anger/texts_count),2) * 100
    per_cent_fear = round((texts_fear/texts_count),2) * 100
    per_cent_love = round((texts_love/texts_count),2) * 100
    per_cent_surprise = round((texts_surprise/texts_count),2) * 100

    context = {
        'texts_count' : texts_count,
        'users_count' : users_count,
        'users' : users,
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

    
    if 'date1' and 'date2' in request.GET and request.GET['date1'] != '' and request.GET['date2'] != '':
        import datetime
        date1_input = request.GET['date1']
        date2_input = request.GET['date2']
        date_from = datetime.datetime.strptime(request.GET['date1'], '%Y-%m-%d')
        date_to = datetime.datetime.strptime(request.GET['date2'], '%Y-%m-%d')
        context['result_nb_text'] = Text.objects.filter(created_at__range=(date_from, date_to)).count()
        context['texts_happy'] = Text.objects.filter(created_at__range=(date_from, date_to),emotion="happy").count()
        context['texts_sadness'] = Text.objects.filter(created_at__range=(date_from, date_to),emotion="sadness").count()
        context['texts_anger'] = Text.objects.filter(created_at__range=(date_from, date_to),emotion="anger").count()
        context['texts_fear'] = Text.objects.filter(created_at__range=(date_from, date_to),emotion="fear").count()
        context['texts_love'] = Text.objects.filter(created_at__range=(date_from, date_to),emotion="love").count()
        context['texts_surprise'] = Text.objects.filter(created_at__range=(date_from, date_to),emotion="surprise").count()
        context['date1'] = date1_input
        context['date2'] = date2_input
        context['search'] = True
        context['per_cent_sadness'] = round((context['texts_sadness']/context['result_nb_text']),2) * 100
        context['per_cent_anger'] = round((context['texts_anger']/context['result_nb_text']),2) * 100
        context['per_cent_fear'] = round((context['texts_fear']/context['result_nb_text']),2) * 100
        context['per_cent_love'] = round((context['texts_love']/context['result_nb_text']),2) * 100
        context['per_cent_surprise'] = round((context['texts_surprise']/context['result_nb_text']),2) * 100
        context['per_cent_happy'] = round((context['texts_happy']/context['result_nb_text']),2) * 100
        
    return render(request, 'protected/protected.html', context)


def profilePage(request, pk):
    """
    Display the profile of the current logged in user. It shows informations as well as his own emotion weel

    **parameter**
    request => Any request that can be made in the view

    **return**
    Return the associated view with the render function
    """
    # Get the current logged in user
    current_user = User.objects.get(id=pk)
    # Get the number of texts associated with this user
    texts_user = Text.objects.filter(client=current_user.id)
    texts = Text.objects.filter(client=current_user.id).count()
    # Get the number of texts associated with each emotion: Will be used to create the emotion weel
    texts_happy = Text.objects.filter(client=current_user, emotion="happy").count()
    texts_sadness = Text.objects.filter(client=current_user, emotion="sadness").count()
    texts_anger = Text.objects.filter(client=current_user, emotion="anger").count()
    texts_fear = Text.objects.filter(client=current_user, emotion="fear").count()
    texts_love = Text.objects.filter(client=current_user, emotion="love").count()
    texts_surprise = Text.objects.filter(client=current_user, emotion="surprise").count()
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
        "texts_user" : texts_user,
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
        "current_user" : current_user
    }

    if 'date1' and 'date2' in request.GET and request.GET['date1'] != '' and request.GET['date2'] != '':
        import datetime
        date1_input = request.GET['date1']
        date2_input = request.GET['date2']
        date_from = datetime.datetime.strptime(request.GET['date1'], '%Y-%m-%d')
        date_to = datetime.datetime.strptime(request.GET['date2'], '%Y-%m-%d')
        context['texts_search'] = Text.objects.filter(created_at__range=(date_from, date_to))
        context['result_nb_text'] = Text.objects.filter(created_at__range=(date_from, date_to)).count()
        context['texts_happy'] = Text.objects.filter(created_at__range=(date_from, date_to),emotion="happy").count()
        context['texts_sadness'] = Text.objects.filter(created_at__range=(date_from, date_to),emotion="sadness").count()
        context['texts_anger'] = Text.objects.filter(created_at__range=(date_from, date_to),emotion="anger").count()
        context['texts_fear'] = Text.objects.filter(created_at__range=(date_from, date_to),emotion="fear").count()
        context['texts_love'] = Text.objects.filter(created_at__range=(date_from, date_to),emotion="love").count()
        context['texts_surprise'] = Text.objects.filter(created_at__range=(date_from, date_to),emotion="surprise").count()
        context['date1'] = date1_input
        context['date2'] = date2_input
        context['search'] = True
        context['per_cent_sadness'] = round((context['texts_sadness']/context['result_nb_text']),2) * 100
        context['per_cent_anger'] = round((context['texts_anger']/context['result_nb_text']),2) * 100
        context['per_cent_fear'] = round((context['texts_fear']/context['result_nb_text']),2) * 100
        context['per_cent_love'] = round((context['texts_love']/context['result_nb_text']),2) * 100
        context['per_cent_surprise'] = round((context['texts_surprise']/context['result_nb_text']),2) * 100
        context['per_cent_happy'] = round((context['texts_happy']/context['result_nb_text']),2) * 100

    return render(request, 'protected/profile_admin.html', context)


def profileTextView(request, pk):

    # Get the current text
    current_text = Text.objects.get(id=pk)
    context = {}
    context['text'] = current_text
    context['current_user'] = current_text

    return render(request, 'protected/profile_text_detail.html', context)





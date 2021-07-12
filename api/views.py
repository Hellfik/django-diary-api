from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .serialiser import TextSerialiser, UserSerialiser
from rest_framework import status
from base.models import Text
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


# Create your views here.
@csrf_exempt
@api_view(['GET',])
@permission_classes([IsAuthenticated])
def apiOverView(request):
    api_urls = {
        'text_List': '/texts',
        'details_view': '/text/<int:pk>',
        'create': '/text/create',
        'delete': '/text/delete/<int:pk>',
        'update': '/text/update/<int:pk>'
    }
    return Response(api_urls)

# TEXT API

# Get the list of all texts


@api_view(['GET',],)
#@permission_classes([IsAuthenticated])
@csrf_exempt
def TextList(request):
    texts = Text.objects.all()
    serialiser = TextSerialiser(texts, many=True)
    return Response(serialiser.data)

# Get the detail of only one text based on its id


@api_view(['GET',])
#@permission_classes([IsAuthenticated])
@csrf_exempt
def TextDetail(request, pk):
    try:
        text = Text.objects.get(id=pk)
    except Text.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serialiser = TextSerialiser(text, many=False)
        return Response(serialiser.data)

# Update one text based on its id


@csrf_exempt
@api_view(['PUT',])
@permission_classes([IsAuthenticated])
def TextUpdate(request, pk):
    try:
        text = Text.objects.get(id=pk)
    except Text.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serialiser = TextSerialiser(text, data=request.data)
        data = {}
        if serialiser.is_valid():
            serialiser.save()
            data['success'] = "Update successful"
            return Response(data=data)
    return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete one text based on its id


@csrf_exempt
@api_view(['DELETE',])
@permission_classes([IsAuthenticated])
def TextDelete(request, pk):
    try:
        text = Text.objects.get(id=pk)
    except Text.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        operation = text.delete()
        data = {}
        if operation:
            data['success'] = "delete successful"
        else:
            data['failure'] = "delete failed"
    return Response(data=data)


@csrf_exempt
@api_view(['POST',])
@permission_classes([IsAuthenticated])
def TextCreate(request):
    user = User.objects.get(pk=1)


# USER API

# Get the list of all users
@csrf_exempt
@api_view(['GET',])
#@permission_classes([IsAuthenticated])
def UserList(request):
    if request.method == 'GET':
        users = User.objects.all()
        serialiser = UserSerialiser(users, many=True)
    return Response(serialiser.data)

# Get the detail of only one user based on its id

@csrf_exempt
@api_view(['GET',])
@permission_classes([IsAuthenticated])
def UserDetail(request, pk):
    if request.method == 'GET':
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

        serialiser = UserSerialiser(user, many=False)
        return Response(serialiser.data)


@csrf_exempt
@api_view(['POST',])
@permission_classes([IsAuthenticated])
def registration_view(request):

    if request.method == 'POST':
        serialiser = UserSerialiser(data=request.data)
        data = {}
        if serialiser.is_valid():
            user = serialiser.save()
            data['response'] = "Succesfully registered a new user"
            data['username'] = user.username
        else:
            data = serialiser.errors
        return Response(data)


# Delete one text based on its id
@csrf_exempt
@api_view(['DELETE',])
#@permission_classes([IsAuthenticated])
def UserDelete(request, pk):
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        operation = user.delete()
        data = {}
        if operation:
            data['success'] = "delete successful"
        else:
            data['failure'] = "delete failed"
    return Response(data=data)

@csrf_exempt
@api_view(['PUT',])
@permission_classes([IsAuthenticated])
def UserUpdate(request, pk):
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serialiser = UserSerialiser(user, data=request.data)
        data = {}
        if serialiser.is_valid():
            serialiser.save()
            data['success'] = "Update successful"
            return Response(data=data)
    return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)



###########################################################################                                                                        #
#                                API                                      #
###########################################################################

import requests

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required(login_url='login')
def apiGetUsers(request):
    url = "http://127.0.0.1:8000/api/user-list"
    reponse = requests.get(url)
    users = reponse.json()
    context = {}
    context['users'] = users
    return context
    
@staff_member_required(login_url='login')
def apiGetTexts(request):
    url = "http://127.0.0.1:8000/api/text-list"
    reponse = requests.get(url)
    texts = reponse.json()
    context = {}
    context['texts'] = texts
    
    return context

@staff_member_required(login_url='login')
def apiGetText(request):
    context = {}
    if 'text_id' in request.GET:
        text_id = request.GET['text_id']
        url = "http://127.0.0.1:8000/api/text-detail/%s" % text_id
        response = requests.get(url)
        text = response.json()
        context['text'] = text
    
    return context

@staff_member_required(login_url='login')
def dashboardViewApi(request):
    
    texts = apiGetTexts(request)['texts']
    users = apiGetUsers(request)['users']

    texts_happy = len([text for text in texts if text['emotion'] == 'happy'])
    texts_sadness = len([text for text in texts if text['emotion'] == 'sadness'])
    texts_fear = len([text for text in texts if text['emotion'] == 'fear'])
    texts_surprise = len([text for text in texts if text['emotion'] == 'surpise'])
    texts_love = len([text for text in texts if text['emotion'] == 'love'])
    texts_anger = len([text for text in texts if text['emotion'] == 'anger'])

    texts_count = len(texts)
    users_count = len(users)

    # Translation in percentage
    per_cent_happy = round((texts_happy/texts_count),2) * 100
    per_cent_sadness = round((texts_sadness/texts_count),2) * 100
    per_cent_anger = round((texts_anger/texts_count),2) * 100
    per_cent_fear = round((texts_fear/texts_count),2) * 100
    per_cent_love = round((texts_love/texts_count),2) * 100
    per_cent_surprise = round((texts_surprise/texts_count),2) * 100

    context = {
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

    context['users'] = users
    context['texts'] = texts
    context['texts_count'] = texts_count
    context['users_count'] = users_count

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

    return render(request, 'api/api_dashboard.html', context)


@staff_member_required(login_url='login')
def apiDeleteUser(request):
    context = {}
    if 'user_id' in request.GET:
        user_id = request.GET['user_id']
        url = "http://127.0.0.1:8000/api/user-delete/%s" % user_id
        response = requests.get(url)
        user = response.json()
        context['user'] = user
    
    return context


#####################
#    MODELVIEWSET   #
#####################

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerialiser
    queryset = User.objects.all()


class TextViewSet(viewsets.ModelViewSet):
    serializer_class = TextSerialiser
    queryset = Text.objects.all()

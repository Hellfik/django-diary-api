from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import serializers
from rest_framework.decorators import api_view, renderer_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import set_rollback
from .serialiser import TextSerialiser, UserSerialiser
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework import status
from base.models import Text
from django.contrib.auth.models import User


# Create your views here.
@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'text_List' : '/texts',
        'details_view' : '/text/<int:pk>',
        'create' : '/text/create',
        'delete' : '/text/delete/<int:pk>',
        'update' : '/text/update/<int:pk>'
    }
    return Response(api_urls)

# TEXT API

# Get the list of all texts
@api_view(['GET'],)
@csrf_exempt
def TextList(request):
    texts = Text.objects.all()
    serialiser = TextSerialiser(texts, many=True)
    return Response(serialiser.data)

# Get the detail of only one text based on its id
@api_view(['GET'])
@csrf_exempt
def TextDetail(request, pk):
    try:
        text = Text.objects.get(id=pk)
    except Text.DoesNotExist: 
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    serialiser = TextSerialiser(text, many=False)
    return Response(serialiser.data)

# Update one text based on its id
@csrf_exempt
@api_view(['PUT'])
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
            data['sucess'] = "Update successful"
            return Response(data=data)
    return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete one text based on its id
@csrf_exempt
@api_view(['DELETE'])
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
@api_view(['POST'])
def TextCreate(request):
    user = User.objects.get(pk=1)



# USER API

# Get the list of all users
@api_view(['GET'])
def UserList(request):
    if request.method == 'GET':
        users = User.objects.all()
        serialiser = UserSerialiser(users, many=True)
    return Response(serialiser.data)

# Get the detail of only one user based on its id
@api_view(['GET'])
def UserDetail(request, pk):
    if request.method == 'GET':
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

        serialiser = UserSerialiser(user, many=False)
        return Response(serialiser.data)


@csrf_exempt
@api_view(['POST'])
def registration_view(request):

    if request.method == 'POST':
        serialiser = UserSerialiser(data=request.data)
        data = {}
        if serialiser.is_valid():
            user = serialiser.save()
            data['response'] = "succesfully registers a new user"
            data['email'] = user.email
            data['username'] = user.username
        else:
            data = serialiser.errors
        return Response(data)
from django.urls import path
from rest_framework.decorators import api_view
from .views import TextDelete, TextUpdate, UserDelete, UserUpdate ,apiOverView, TextList, UserList, TextDetail, UserDetail, TextCreate, registration_view, UserDelete
from rest_framework import routers

#router = routers.DefaultRouter()
#router.register('api', apiOverView)

# All urls for the API app
urlpatterns = [
    # API Text
    path('', apiOverView, name='api'),
    path('text-list/', TextList, name="api-text-list"),
    path('text-detail/<int:pk>', TextDetail, name="api-text-detail"),
    path('text-create/', TextCreate, name='api-text-create'),
    path('text-update/<int:pk>', TextUpdate, name='api-text-update'),
    path('text-delete/<int:pk>', TextDelete, name='api-text-delete'),
    # API User,
    path('user-list/', UserList, name='api-user-list'),
    path('user-detail/<int:pk>', UserDetail, name="api-user-detail"),
    path('user-registration', registration_view, name="api-user-registration"),
    path('user-delete/<int:pk>', UserDelete, name="api-user-delete"),
    path('user-update/<int:pk>', UserUpdate, name="api-user-update")
]
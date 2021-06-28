from django.urls import path

from .views import CustomLoginView, RegisterView, TextDetail, TextList, TextCreate, TextUpdate, TextDelete, homePage, profilePage
from django.contrib.auth.views import LogoutView

# All urls for the base app
urlpatterns = [
    path('', homePage, name='home'),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', profilePage, name='profile'),
    path('texts/', TextList.as_view(), name="texts"),
    path('text/<int:pk>/', TextDetail.as_view(), name="text"),
    path('text/create/', TextCreate.as_view(), name="text-create"),
    # int:pk is used to retrieve an item based on it's id (or primary key)
    path('text/update/<int:pk>/', TextUpdate.as_view(), name='text-update'),
    path('text/delete/<int:pk>/', TextDelete.as_view(), name='text-delete'),
]
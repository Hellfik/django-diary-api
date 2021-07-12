##############
#   IMPORT   #
##############

from django.urls import path, include
from rest_framework.decorators import api_view
from .views import (
    TextList, 
    TextDetail, 
    TextCreate, 
    TextUpdate, 
    TextDelete, 
    UserList, 
    UserDetail, 
    UserDelete, 
    UserUpdate,
    dashboardViewApi,
    registration_view,  
    apiOverView,
    UserViewSet,
    TextViewSet,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('texts', TextViewSet, basename='texts')
#urlpatterns = router.urls


##################
#    API URLS    #
##################

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
    path('user-update/<int:pk>', UserUpdate, name="api-user-update"),
    path('admin/', dashboardViewApi, name="api-texts"),
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('api-user-delete/', apiDeleteUser, name='user-delete')
]
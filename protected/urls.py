from base.views import profilePage
from django.urls import path
from .views import protectedView, CustomLoginView, profilePage, profileTextView

urlpatterns = [
    path('', CustomLoginView.as_view(), name="login_admin"),
    path('admin/', protectedView, name="protected_admin"),
    path('user/<int:pk>' ,profilePage, name="profile_admin"),
    path('text/<int:pk>', profileTextView, name="profile_text_user")
]
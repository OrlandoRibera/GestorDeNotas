from django.urls import path

from registration.views import SignUpView

urlpatterns = [
    path('signup/',  SignUpView.as_view(), name='signup'),
]

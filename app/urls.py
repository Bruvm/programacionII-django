from django.urls import path
from .views import UserView, RoleView, hello_world

urlpatterns = [
    path('', hello_world),
    path('users/', UserView.as_view()),   
    path('roles/', RoleView.as_view()),
]
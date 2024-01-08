from django.urls import path
from .views import user_registration, user_login, user_logout, home, index

urlpatterns = [
    path('', index, name='index'),
    path('registration/', user_registration, name='registration'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('home/', home, name='home'),
]
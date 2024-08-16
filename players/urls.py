from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.players_list, name='players'),
    path('signup', views.signup, name='signup'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('accounts/', include('django.contrib.auth.urls')),
]

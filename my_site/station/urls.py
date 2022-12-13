from django.urls import path
from . import views

app_name = 'station'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('loading_data/', views.loading_data, name='loading_data'),
    path('data_addition/', views.data_addition, name='data_addition'),
    path('statistics/', views.statistics, name='statistics'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]


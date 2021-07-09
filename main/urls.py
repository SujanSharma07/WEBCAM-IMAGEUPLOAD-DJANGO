
from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('saveimage/', saveimage, name='saveimage'),
    path('all/', viewall, name='all'),

]

from app1.views import *
from django.urls import path
app_name='goodgirl'
urlpatterns=[
    path('sumi/',sumi,name='sumi')
]
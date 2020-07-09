from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage,name='mainpage'),
    path('create/',views.create, name='create'),
    path('update/',views.update, name='update'),
    path('wholelist/',views.wholelist,name='wholelist')
]
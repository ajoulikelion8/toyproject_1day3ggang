from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.mainpage,name='mainpage'),
    path('create/',views.create, name='create'),
    path('wholelist/',views.wholelist,name='wholelist'),
    path('detail/<int:list_id>/',views.detail,name='detail'),
    path('delete/<int:list_id>/',views.delete,name='delete'),
    # path('edit/<int:list_id>/',views.edit,name='edit'),
    path('update/<int:list_id>/',views.update,name='update'),
]
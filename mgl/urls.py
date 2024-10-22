from django.urls import path
from mgl.views import GameListView

urlpatterns = [
    path('mygamelist/', GameListView, name='index'),  
    #path('mygamelist/register/', RegisterFormView.as_view(),  name='register'),
]


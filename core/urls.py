from django.urls import path,include
from core.views import home, update,delete,mywatchlist

urlpatterns = [
    path('',home,name='home'),
    path('update/<int:list_id>/',update, name='update'),
    path('mywatchlist/',mywatchlist, name='mywatchlist'),
    path('delete/<int:list_id>/',delete, name='delete')
    
]

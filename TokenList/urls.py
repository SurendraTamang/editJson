from django.urls import path
from TokenList import views

urlpatterns = [
    path('',views.index, name="index")
]

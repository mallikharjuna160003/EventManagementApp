from django.urls import path, include
from authapp import views

urlpatterns = [
    path('',include('djoser.urls')),
    path('',include('djoser.urls.authtoken')),
    
    path('EventList/',views.EventList),
    path('EventCreate/',views.EventCreate),
    path('EventUpdate/<str:pk>/',views.EventUpdate),
    path('EventDetail/<str:pk>/',views.EventDetail),
    path('EventDelete/<str:pk>/',views.EventDelete),
    #path('EventFilter/',views.EventFilter),
    #path('EventFilterDateRange/',views.EventFilterDateRange),
   
]
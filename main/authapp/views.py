from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from .models import Events
from .serializers import EventSerializer
#from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
import datetime


#Get the All events list of authenticated user
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def EventList(request):
    eventslist = Events.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'iscompleted']
    serializer = EventSerializer(eventslist, many=True)
    return Response(serializer.data)


#Get the particular event details by pk:id
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def EventDetail(request, pk):
    eventslist = Events.objects.get(id=pk)
    serializer = EventSerializer(eventslist, many=False)
    return Response(serializer.data)


#Create the event 
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def EventCreate(request):
    serializer = EventSerializer( data=request.data)
    if serializer.is_valid():
        print("data saved")
        serializer.save()
    else:
        print("Not valid")
    return Response(serializer.data)


 
#Update the event by pk:id
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def EventUpdate(request,pk):
    eventslist = Events.objects.get(id=pk)
    serializer = EventSerializer(instance = eventslist, data=request.data)
    if serializer.is_valid():
        print("Update Not valid")
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)


#delete the event by id
@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def EventDelete(request,pk):
    eventslist = Events.objects.get(id=pk)
    eventslist.delete()
    return Response({"msg":"Event Deleted"})

"""
#filter by type iscompleted or not  and filter by date 

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def EventFilter(request):
    eventslist = Events.objects.all()
    serializer = EventSerializer(eventslist, many=True)
    filter_backends = (DjangoFilterBackend,SearchFilter)
    #filter by startDateTime and endDateTime and iscompleted
    filter_fields = ('startDateTime','endDateTime','iscompleted')
    search_fields = ('startDateTime','endDateTime','iscompleted')
    return Response(serializer)

#filter by  filter by date range

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def EventFilterDateRange(request):
    filter_backends = (DjangoFilterBackend,)
    #for filtering the range of dates
    if request.method = 'POST':
        fromdate = request.POST.get('fromDateTime')
        todate = request.POST.get('toDateTime')
        filter_eventlist = Events.objects.filter(startDateTime__gte=datetime(fromdate), startDateTime__lt=datetime(todate))
        serializer2 = EventSerializer(filter_eventlist,many=True) #serialization
        return Response(serializer2)
    
"""



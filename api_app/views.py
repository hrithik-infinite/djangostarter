from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from rest_framework import status
from .serializers import CartItemsSerializer, CricketTeamListSerializer
from .models import CartItems, CricketTeamSheet
from django.shortcuts import get_object_or_404
from django.urls import reverse

class CartItemViews(APIView):
    # This is equivalent to the @RestController in used in Java.
    def post(self, request):
        # Extracting the request body from the post request.
        serializer = CartItemsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status" : "success", "data" : serializer.data}, status = status.HTTP_200_OK)
        return Response({"status" : "Error", "data" : serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, id = None):
        if id:
            item = CartItems.objects.get(id = id)
            serializer = CartItemsSerializer(item)
        else:  
            items = CartItems.objects.all()
            serializer = CartItemsSerializer(items, many = True)
        return Response({"status" : "Success", "data" : serializer.data}, status = status.HTTP_200_OK)
    
    def patch(self, request, id = None):
        # Extracting the partial request body from the patch request.
        item = CartItems.objects.get(id = id)
        serializer = CartItemsSerializer(item, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status" : "success", "data" : serializer.data}, status = status.HTTP_200_OK)
        return Response({"status" : "Error", "data" : serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id = None):
        # Extracting the request body from the delete request.
        item = get_object_or_404(CartItems, id = id)
        item.delete()
        return Response({"status" : "success", "data" : "Item with id " + str(id) + " deleted successfully."}, status = status.HTTP_200_OK)
    
    
    
class CricketTeamListView(APIView):
    # This is equivalent to the @RestController in used in Java.
    def post(self, request):
        # Extracting the request body from the post request.
        serializer = CricketTeamListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status" : "success", "data" : serializer.data}, status = status.HTTP_200_OK)
        return Response({"status" : "Error", "data" : serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, id = None):
        if id:
            item = CricketTeamSheet.objects.get(id = id)
            serializer = CricketTeamListSerializer(item)
            context = {
                'mychild' : item
            }
        else:  
            items = CricketTeamSheet.objects.all()
            serializer = CricketTeamListSerializer(items, many = True)
            context = {
                'mychild' : items
            }
        template = loader.get_template("cricket.html")
        return HttpResponse(template.render(context, request))
    
    def patch(self, request, id = None):
        # Extracting the partial request body from the patch request.
        item = CricketTeamSheet.objects.get(id = id)
        serializer = CricketTeamListSerializer(item, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status" : "success", "data" : serializer.data}, status = status.HTTP_200_OK)
        return Response({"status" : "Error", "data" : serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id = None):
        # Extracting the request body from the delete request.
        item = get_object_or_404(CricketTeamSheet, id = id)
        item.delete()
        return HttpResponseRedirect(reverse('cricket'))

def addPlayer(request):
    template = loader.get_template("cricketadd.html")
    return HttpResponse(template.render({}, request))

def addAPlayerRecord(request):
    first = request.POST['first']
    last = request.POST['last']
    team = request.POST['team']
    role = request.POST['role']
    child = CricketTeamSheet(firstName = first,lastName =  last,cricketTeam =  team, role = role)
    child.save()
    return HttpResponseRedirect(reverse('api/cricket'))


def cricketdelete(request, id):
    mychild = CricketTeamSheet.objects.get(id=id)
    mychild.delete()
    return HttpResponseRedirect(reverse('cricket'))

def cricketupdate(request, id):
    mychild = CricketTeamSheet.objects.get(id=id)
    template = loader.get_template("cricketupdate.html")
    context = {
        'mychild' : mychild
    }
    return HttpResponse(template.render(context, request))

def cricketupdaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    team = request.POST['team']
    role = request.POST['role']
    # print(team )
    mychild = CricketTeamSheet.objects.get(id=id)
    mychild.firstName = first
    mychild.lastName = last
    mychild.cricketTeam = team
    mychild.role = role
    mychild.save()
    return HttpResponseRedirect(reverse('cricket'))
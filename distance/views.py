from distance.models import Client, Destination
from distance.serializers import ClientSerializer, DestinationSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from math import radians, sin, cos, acos
from django.views.generic import ListView
from django.http import HttpResponse


class ClientList(APIView):
    """
    List all clients, or create a new client.
    """
    def get(self, request, format=None):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientDetail(APIView):
    """
    Retrieve, update or delete a client instance.
    """
    def get_object(self, pk):
        try:
            return Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        client = self.get_object(pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        client = self.get_object(pk)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        client = self.get_object(pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DestinationList(APIView):
    """
    List all destinations, or create a new destination.
    """
    def get(self, request, format=None):
        destinations = Destination.objects.all()
        serializer = DestinationSerializer(destinations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DestinationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DestinationDetail(APIView):
    """
    Retrieve, update or delete destination instance.
    """
    def get_object(self, pk):
        try:
            return Destination.objects.get(pk=pk)
        except Destination.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        destination = self.get_object(pk)
        serializer = DestinationSerializer(client)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        destination = self.get_object(pk)
        serializer = DestinationSerializer(destination, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        destination = self.get_object(pk)
        destination.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# Python 3 program to calculate Distance Between Two Points on Earth
from math import radians, cos, sin, asin, sqrt
def distance(lat1, lat2, lon1, lon2):
	
	# The math module contains a function named
	# radians which converts from degrees to radians.
	lon1 = radians(lon1)
	lon2 = radians(lon2)
	lat1 = radians(lat1)
	lat2 = radians(lat2)
	
	# Haversine formula
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2

	c = 2 * asin(sqrt(a))
	
	# Radius of earth in kilometers. Use 3956 for miles
	r = 6371
	
	# calculate the result
	return(c * r)
	
	
# driver code
lat1 = 53.32055555555556
lat2 = 53.31861111111111
lon1 = -1.7297222222222221
lon2 = -1.6997222222222223
print(distance(lat1, lat2, lon1, lon2), "K.M")


def distance(request):
	slat= '', 
	slon= '', 
	elat= '', 
	elon= ''
	dist= ''
	client =Client.objects.filter(pk=request.user.pk)  
	destination =Destination.objects.filter(pk=request.user.pk)  
	slat = client
	slon = client 
	elat = destination 
	elon = destination
	dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
	context={
		slat:slat,
		slon:slon,
		elat:elat,
		elon:elon,
		dist:dist
	}
	return render(request, 'distance.html', context)
	
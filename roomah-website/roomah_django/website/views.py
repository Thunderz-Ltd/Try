from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

from .models import House, UserProfile
from .serializers import HouseSerializer, HousemateSerializer

class HouseList(viewsets.ModelViewSet):
    
    queryset = House.objects.all()
    serializer_class = HouseSerializer
        

class HouseDetail(APIView):
    def get_object(self, house_slug):
        try:
            return House.objects.get(id=house_slug)
        except House.DoesNotExist:
            raise Http404
    
    def get(self, request, house_slug, format=None):
        house = self.get_object(house_slug)
        serializer = HouseSerializer(house)
        return Response(serializer.data)

class HousemateList(viewsets.ModelViewSet):

    # if viewsets.ModelViewSet == 'POST':
    #     profilephoto = viewsets.ModelViewSet.FILES.get('profilephoto')
    
    queryset = UserProfile.objects.all()
    serializer_class = HousemateSerializer

class HousemateDetail(APIView):
    def get_object(self, housemate_slug):
        try:
            return UserProfile.objects.get(username=housemate_slug)
        except UserProfile.DoesNotExist:
            raise Http404
    
    def get(self, request, housemate_slug, format=None):
        housemate = self.get_object(housemate_slug)
        serializer = HousemateSerializer(housemate)
        return Response(serializer.data)

        

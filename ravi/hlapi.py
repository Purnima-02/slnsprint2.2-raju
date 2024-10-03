from rest_framework import viewsets
from ravi.hlserializers import hlApplicationSerializer,plApplicationSerializer
from .models import *
class CustomerViewSet(viewsets.ModelViewSet):
    queryset=CustomerProfile.objects.all()
    serializer_class=hlApplicationSerializer



class PlViewSet(viewsets.ModelViewSet):
    queryset=PersonalDetail.objects.all()
    serializer_class=plApplicationSerializer
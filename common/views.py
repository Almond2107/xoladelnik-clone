from rest_framework import generics
from .models import Sponsor
from .serializers import SponsorSerializer


class SponsorListCreateView(generics.ListCreateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


class SponsorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer

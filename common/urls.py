from django.urls import path
from .views import SponsorListCreateView, SponsorRetrieveUpdateDestroyView

urlpatterns = [
    path("sponsors/", SponsorListCreateView.as_view(), name="sponsor-list-create"),
    path("sponsors/<int:pk>/", SponsorRetrieveUpdateDestroyView.as_view(), name="sponsor-detail"),
]

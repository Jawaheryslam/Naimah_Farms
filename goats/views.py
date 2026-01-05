from rest_framework import viewsets
from .models import Goat
from .serializers import GoatSerializer


class GoatViewSet(viewsets.ModelViewSet):
    queryset = Goat.objects.all()
    serializer_class = GoatSerializer

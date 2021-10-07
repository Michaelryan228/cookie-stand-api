from rest_framework import generics
from .serializers import Cookie_StandSerializer
from .models import Cookie_Stand
from .permissions import IsOwnerOrReadOnly


class Cookie_StandList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Cookie_Stand.objects.all()
    serializer_class = Cookie_StandSerializer


class Cookie_StandDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Cookie_Stand.objects.all()
    serializer_class = Cookie_StandSerializer

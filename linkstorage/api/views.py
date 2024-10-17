from rest_framework import viewsets
from .models import Link, Collection
from linkstorage.serializers import CollectionSerializer, LinkSerializer



class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


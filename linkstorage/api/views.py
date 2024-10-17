from rest_framework import viewsets
from rest_framework.response import Response
from linkstorage.utils import fetch_open_graph_data
from .models import Link, Collection
from linkstorage.serializers import CollectionSerializer, LinkSerializer


class LinkViewSet(viewsets.ModelViewSet):
    serializer_class = LinkSerializer

    def get_queryset(self):
        return Link.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        url = serializer.validated_data['url']
        og_data = fetch_open_graph_data(url)
        serializer.save(
            title=og_data['title'],
            description=og_data['description'],
            image=og_data['image'],
            link_type=og_data['type'],
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        url = serializer.validated_data.get('url', None)
        if url:
            self.perform_create(serializer)
        else:
            serializer.save()


class CollectionViewSet(viewsets.ModelViewSet):
    serializer_class = CollectionSerializer

    def get_queryset(self):
        user = self.request.user
        return Collection.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

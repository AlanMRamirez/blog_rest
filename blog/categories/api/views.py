from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from categories.models import Category
from categories.api.serializers import CategorySerializer
from categories.api.permissions import IsAdminOrReadOnly

#This class create a CRUD
class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    #queryset = Category.objects.all()
     
    
    #Only return published values
    queryset = Category.objects.filter(published=True)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['published', 'title']

    
    lookup_field = 'slug'
    




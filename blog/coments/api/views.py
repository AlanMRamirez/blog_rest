from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from coments.models import Comment
from coments.api.serializers import CommentSerializer
from coments.api.permissions import IsOwnerOrReadCreateOnly

class CommentApiViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadCreateOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering = ['-created']
    filterset_fields = ['post']



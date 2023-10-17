from rest_framework import viewsets, permissions, mixins, filters
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404

from posts.models import Post, Group
from api.serializers import (
    PostSerializer, CommentSerializer, GroupSerializer,
    FollowSerializer
)
from api.permission import OwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """
    Класс PostViewSet. Осуществляет проверку на автора поста.
    Назначает автора при создании поста.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (OwnerOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FollowViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    Класс FollowViewSet.
    Позволяет подписаться на другого пользователя.
    """
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.followers.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Класс GoupViewSet. Работает с группами. Реализован только для чтения.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.AllowAny,)


class CommentViewSet(viewsets.ModelViewSet):
    """
    Класс CommentViewSet. Создает комментарии к постам.
    Осуществляет проверку на автора комментария.
    """
    serializer_class = CommentSerializer
    permission_classes = (OwnerOrReadOnly,)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        serializer.save(post=get_object_or_404(
            Post, pk=self.kwargs.get('post_id')), author=self.request.user
        )

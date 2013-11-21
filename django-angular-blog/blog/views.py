from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import generic

from rest_framework import permissions, viewsets

from .models import Post, Category
from .serializers import PostSerializer, UserSerializer, CategorySerializer
from .permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """
	This viewset automatically provides 'list', 'create', 'retrieve',
	'update', and 'destroy' actions.
	"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class CategoryViewSet(viewsets.ModelViewSet):
    """
	This viewset automatically provides 'list', 'create', 'retrieve',
	'update', and 'destroy' actions.
	"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


def angular_view(request):
    if request.GET.get('_escaped_fragment_'):
        return HttpResponseRedirect(request.GET.get('_escaped_fragment_'))
    else:
        return render(request, 'blog/angular/index.html')


def angular_view_post_list(request):
    return render(request, 'blog/angular/partials/post-list.html')


def angular_view_post_detail(request):
    return render(request, 'blog/angular/partials/post-detail.html')


class PostList(generic.ListView):
    model = Post
    paginate_by = 10


class PostDetail(generic.DetailView):
    model = Post





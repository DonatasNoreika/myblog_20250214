from django.shortcuts import render
from django.views import generic
from .models import Post, Comment
from django.db.models import Q


# Create your views here.
class PostListView(generic.ListView):
    model = Post
    template_name = "posts.html"
    context_object_name = "posts"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "post.html"
    context_object_name = "post"


def search(request):
    query = request.GET.get('query')
    context = {
        "posts": Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)),
        "query": query,
    }
    return render(request, template_name="search.html", context=context)

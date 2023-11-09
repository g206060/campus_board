from django.views import generic

from .models import Board, Post

class IndexView(generic.ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 3
    
class DetailView(generic.DetailView):
    model = Post
    slug_field = "post_title"
    slug_url_kwarg = "post_title"
    
class PostDetailView(generic.DetailView):
    model = Post
    template_name = "post_detail.html"
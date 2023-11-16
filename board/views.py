from django.views import generic
from django.urls import reverse_lazy

from .models import Board, Post

from .forms import PostCreateForm


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
    
class PostCreateView(generic.CreateView):
    model = Post
    template_name = "post_create.html"
    form_class = PostCreateForm
    success_url = reverse_lazy('board:index')
    
    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return super().form_valid(form)
        
    def form_invalid(self, form):
        return super().form_invalid(form)
    
class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = 'post_update.html'
    form_class = PostCreateForm
    
    def get_success_url(self):
        return reverse_lazy('board:post_detail', kwargs={'pk': self.kwargs['pk']})
        
    def form_valid(self, form):
        # messeges.success(self.request, '掲示を更新しました。')
        return super().form_valid(form)
        
    def form_invalid(self, form):
        # messeges.error(self.request, '掲示の更新に失敗しました。')
        return super().form_invalid(form)

class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('board:index')
    
    def delete(self, request, *args, **kwargs):
        # messages.success(self.request, '掲示を削除しました。')
        return super().delete(request, *args, **kwargs)
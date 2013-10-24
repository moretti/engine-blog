from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from blog.models import Post

from django.core.urlresolvers import reverse_lazy


class PostList(ListView):
    model = Post


class PostCreate(CreateView):
    model = Post
    success_url = reverse_lazy('post_list')


class PostUpdate(UpdateView):
    model = Post
    success_url = reverse_lazy('post_list')


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

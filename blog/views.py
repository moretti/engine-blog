from django.views.generic import DetailView, TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from blog.models import Post
from blog.forms import PostForm

from django.core.urlresolvers import reverse_lazy, reverse
from django.template.defaultfilters import slugify

from django.http import HttpResponseRedirect


class PostDetail(DetailView):
    model = Post


class PostList(ListView):
    model = Post
    paginate_by = 5


class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super(PostCreate, self).form_valid(form)


class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        return super(PostUpdate, self).form_valid(form)


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')

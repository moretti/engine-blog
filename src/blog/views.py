
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render_to_response
from django.template.defaultfilters import slugify
from django.views.generic import View, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from blog.forms import PostForm
from blog.models import Post


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


class Archives(View):

    def get(self, request):
        posts = Post.objects.all().order_by('-pub_date')
        return render_to_response('archives.html', {'posts': posts})

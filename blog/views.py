from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
# these are function based views
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog_temp/home.html', context)

def about(request):
    return render(request, 'blog_temp/about.html', {'title':'About'}) 

#these are class based views which give us more features
class PostListView(ListView):
    model = Post
    template_name = 'blog_temp/home.html' # <app> / <model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_temp/post_detail.html'

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'blog_temp/post_form.html'
    fields = ['title', 'content']

    #this method sets the author of the post to the current user which is logged in
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog_temp/post_form.html'
    fields = ['title', 'content']

    #this method sets the author of the post to the current user which is logged in
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog_temp/post_confirm_delete.html'
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
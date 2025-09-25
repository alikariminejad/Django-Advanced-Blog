from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from .models import Post
from django.shortcuts import get_object_or_404
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# a function based view to show index page
"""
def indexView(request):
    name = "Ali"
    context = {"name": name}
    return render(request, "index.html", context)
"""


class IndexView(TemplateView):
    """a class based view to show index page"""
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["name"] = "Ali"
        context["posts"] = Post.objects.all()
        return context
    
# a function based view for redirect
"""
def redirectToMaktab(request):
    return redirect('https://maktabkhooneh.og') 
"""

class RedirectToMaktab(RedirectView):
    url = "https://maktabkhooneh.org"
    
    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])
        print("post: ", post)
        return super().get_redirect_url(*args, **kwargs)
    
class PostList(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    permission_required = 'blog.view_post'
    # different ways to get objects
    # 1 
    model = Post
    # 2
    # queryset = Post.objects.all()
    
    context_object_name = 'posts'
    paginate_by = 2
    ordering = '-id'

    # 3
    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts
    

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    
"""
class PostCreateView(FormView):
    template_name = 'contact.html'
    form_class = PostForm
    success_url = '/blog/post/'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
"""

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    # you can either use fields or form class
    # fields = ['author', 'title', 'content', 'status', 'category', 'published_date', ]
    form_class = PostForm
    success_url = '/blog/post/'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
class PostEditView(LoginRequiredMixin,UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'
    
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = '/blog/post/'
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import PostForm, CommentForm
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(content__icontains=q))
        return qs

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Post created successfully.")
        return super().form_valid(form)

class AuthorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

class PostUpdateView(LoginRequiredMixin, AuthorRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Post updated.")
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin, AuthorRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Post deleted.")
        return super().delete(request, *args, **kwargs)

def post_detail(request, slug):
    from .models import Post
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.select_related("author")
    form = CommentForm()

    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "Please log in to comment.")
            return redirect("login")
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, "Comment added.")
            return redirect(post.get_absolute_url())

    return render(request, "blog/post_detail.html", {"post": post, "comments": comments, "form": form})

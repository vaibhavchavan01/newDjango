from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    data={}
    data['posts']=posts
    return render(request, 'blog/post_list.html',data)
def post_detail(request, pk ):
    data={}
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'posts':post})
    # path('post/new/', views.post_new, name='post_new'),
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Count
from .models import Comment, Post, PostSettings, Author

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')

    context = {
        "post_list": Post.objects.all()
    }
    return render(request, 'index.html', context=context)

def detail(request, post_id):
    _post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=_post)
    context = {"post": _post, "comments": comments}
    return render(request, "detail.html", context=context)

def create(request):
    if request.method == "POST":
        form_data = request.POST
        post_settings, _ = PostSettings.objects.get_or_create()
        title = form_data['title']
        text = form_data['text']
        if len(text) > post_settings.text_len or len(title) > post_settings.title_len:
            pass
        else: 
            author, _ = Author.objects.get_or_create(name=request.user.get_full_name())
            post = Post(text=text, title=title, author=author)
            post.save()
    return redirect('index')
    
def create_comment(request, post_id):
    if request.method == "POST":
        form_data = request.POST
        text = form_data.get("text")
        author, _ = Author.objects.get_or_create(name=request.user.get_full_name())
        post = Post.objects.filter(pk=post_id).first()
        comment = Comment(text=text, post=post, author=author)
        comment.save()
        return redirect('detail', post_id=post_id)
    # No need to render a template here, redirecting to detail view instead
    return redirect('detail', post_id=post_id)

def dashboard(request):
    fresh_posts = Post.objects.all().order_by("-created_at")[:5]
    popular_posts = Post.objects.annotate(num_comments=Count("comment"))
    context = {
        "fresh_posts" : fresh_posts,
        "popular_posts" : popular_posts
    }
    return render(request, "dashboard.html", context=context)

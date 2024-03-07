from django.shortcuts import render
from .models import Post, Comment
from django.db.models import Count,F
from market.user.models import User
from .form import CommentForm

def blog_list(request):
    posts=Post.objects.annotate(
        comment_count=Count("comment"),
        author_name=F("author__username")  #Savol 2 ta modelda ham author obyekti bor F qaysi birini oladi
    ).values('id','title','image','content','post_date','comment_count','author_name')
    print(posts)
    context={
        'posts':posts
    }
    return render(request,'temp_blog/blog_full.html',context)


def blog_detail(request,pk):
    
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment=form.save()
            comment.post=Post.objects.get(id=pk)
            comment.author=request.user
            comment.save()
    post=Post.objects.annotate(
        comment_count=Count("comment"),
        author_name=F("author__username")  
    ).filter(pk=pk).values('id','title','image','content','post_date','comment_count','author_name')

    comments=Comment.objects.filter(post_id=pk).select_related('author').order_by('-comment_date')
    
    
    form=CommentForm()
    context={
        'post':post[0],
        'comments':comments,
        'form':form

    }

    return render(request,'temp_blog/single-post.html',context)
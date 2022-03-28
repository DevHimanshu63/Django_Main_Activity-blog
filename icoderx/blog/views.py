from django.shortcuts import redirect, render,HttpResponse
from blog.models import Post,Blogcomment
from django.contrib import messages
# Create your views here.
def blogHome(request):
    allposts=Post.objects.all()
    context={'allpost':allposts}
    return render(request,'blog/blogHome.html',context)
def blogpost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    comments=Blogcomment.objects.filter(post=post)

    context={'post':post,'comments':comments}

    return render(request,'blog/blogpost.html',context) 


def postcomment(request):
    if request.method=="POST":
        comment=request.POST.get("comment")
        user=request.user
        postsno=request.POST.get("postsno")
        post=Post.objects.get(sno=postsno)
        comment=Blogcomment(comment=comment,user=user,post=post)
        comment.save()
        messages.success(request,"Your comment has submitted!")
        
    return redirect("/blog/{{post.slug}}")
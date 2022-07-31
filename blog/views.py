from django.shortcuts import render,redirect
from .models import Post
from .forms import PostModelForm , PostUpdateForm , CommentForm
from  django.contrib.auth.decorators import login_required

@login_required
def index(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('index')
    else:
        form = PostModelForm()
    context = {
        'posts':posts,
        'form':form
    }
    return render(request,'blog/index.html',context)

def about(request):
    return render(request,'blog/about.html')

@login_required
def post_detail(request,pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.post = post
            instance.save()
            return redirect('post_detail',pk=post.id)
    else:
        form = CommentForm(request.POST)
    context = {
        'post':post , 
        'form': form
    }
    return render(request,'blog/post_detail.html',context)  
@login_required
def post_edit(request,pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        form = PostUpdateForm(request.POST , instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail' , pk=post.id)    
        #since we are trying to return to the post detail of a 
        #particular page, we must past in the pk of the page
    else:
        form = PostUpdateForm( instance=post)  
    context = {
        'post':post,
        'form':form ,
    }
    return render(request,'blog/post_edit.html',context)

@login_required
def post_delete(request,pk):
    post = Post.objects.get(id =pk)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    context ={
        'post':post
    }
    return render(request,'blog/post_delete.html',context)
    

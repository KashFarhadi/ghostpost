from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post


def homepage(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, "homepage.html", {'posts': posts})

def post(request):
    if request.method == 'POST':
            form = PostForm(data=request.POST)
            if form.is_valid():
                data = form.cleaned_data
                boast = Post.objects.create(body=data['post'], type_of_post=data['type_of_post'])
                redirecturl = request.POST.get('redirect', '/')
                return redirect(redirecturl)
    else:
        form = PostForm()
    return render(request, 'postsubmit.html', {'form': form})

def upvote(request, element_id):
    post = Post.objects.get(id=element_id)
    post.upvotes += 1
    post.save()
    return redirect('/')

def downvote(request, element_id):
    post = Post.objects.get(id=element_id)
    post.downvotes += 1
    post.save()
    return redirect('/')

def boasts(request):
    posts = Post.objects.filter(type_of_post = 'Boast')
    return render(request, 'boasts.html', {'posts': posts})

def roasts(request):
    posts = Post.objects.filter(type_of_post = 'Roast')
    return render(request, 'roasts.html', {'posts': posts})

def highestvoted(request):
    posts = Post.objects.order_by('-upvotes')
    return render(request, 'highestvoted.html', {'posts': posts})
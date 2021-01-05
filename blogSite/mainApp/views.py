from django.shortcuts import render,HttpResponse
from mainApp.models import Post

# Create your views here.
def blogpost(request):
     allPosts = Post.objects.all()
     
     context = {'allPosts':allPosts}
     return render(request,'blog/blogpost.html',context)
    

def bloghome(request,slug):
     post = Post.objects.filter(slug = slug).first()
     context = {'post':post}
     return render(request,'blog/bloghome.html',context)
    

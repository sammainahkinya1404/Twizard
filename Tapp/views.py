from django.shortcuts import render,redirect
# from .models import Post
from Tapp.models import Contacts

# Create your views here.
def index(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        msg=request.POST['msg']
        caller=Contacts.objects.create(name=name,email=email,msg=msg)
        caller.save()
        return redirect('index')
        
        
    
    
    return render(request, 'index.html')

# def blog(request):
#     # context=Post.objects.all()
#     return render(request, 'blog.html')

# from django.http import Http404
# def post_list(request):
#     # try:
#     #     post = Post.published.get(id=id)
#     # except Post.DoesNotExist:
#     #     raise Http404("No Post found.")
#     return render(request,'Blog/post/list.html')

# from django.shortcuts import render, get_object_or_404
# # ...
# def post_detail(request, id):
#     # post = get_object_or_404(Post,id=id,status=Post.Status.PUBLISHED)
#     return render(request,'blog/post/detail.html')
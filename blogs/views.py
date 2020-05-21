from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Blog
from django.utils import timezone
from django.http import HttpResponseRedirect

def home(request):
    blogs = Blog.objects
    return render(request,'home.html',{'blogs':blogs})


@login_required(login_url="signup")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body']:
            blog =Blog()
            blog.title=request.POST['title']
            blog.body=request.POST['body']
            blog.pub_date=timezone.datetime.now()
            blog.hunter = request.user
            blog.save()
            return redirect('/blogs/'+str(blog.id))
        else:
            return render(request,'create.html',{'error':'Enter All Fields'})
    else:
        return render(request,'create.html')

def detail(request,blog_id):
    x = Blog.objects
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request,'detail.html',{'blog':blog,'x':x})









def delete_view(request, blog_id):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # fetch the object related to passed id
    obj = get_object_or_404(Blog, pk = blog_id)


    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")

    return render(request, "delete_view.html", context)

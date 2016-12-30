from django.shortcuts import render
from blogapp.models import blog,comment,tag,blog_user

def index(request):

    obj = blog.objects

    blog_list = obj.order_by('-creat_time')

    comments = obj.order_by('-comments')

    return render(request,'index.html', {"blog_list": blog_list,"comments":comments})


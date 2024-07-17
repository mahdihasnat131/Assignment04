from django.shortcuts import render
# from posts.models import Post
from task.models import Task
from category.models import Category

def home(request):
    data1= Task.objects.all()
    
    data2= Category.objects.all()

    return render(request, 'home.html',{'data1':data1, 'data2':data2})
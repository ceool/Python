from django.shortcuts import render
from django.http import HttpResponse
 
from .models import Blog
  
  # Create your views here.
def index(request):
    blogs = Blog.objects.all() #Candidate에 있는 모든 객체를 불러와 candidates에 저장
    context = {'blogs':blogs}
    

    return render(request, 'polls/index.html', context)

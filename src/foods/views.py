from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Category,Food

# Create your views here.

def category_list(request):
    categories = Category.objects.all()
    context = {"categories":categories}
    return render(request,'foods/category_list.html',context)

def category_details(request,id):
    category = Category.objects.get(id=id)
    context = {"category":category}
    return render(request,'foods/category_details.html',context)

def food_details(request, id):
    food = Food.objects.get(id=id)
    context = {"food": food}
    return render(request, "foods/food_details.html",context)

def search(request):
    if request.method != "GET":
        raise Http404
    return render(request,'foods/search.html')

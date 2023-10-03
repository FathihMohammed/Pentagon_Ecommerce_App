from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import category,product
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.
def allprocat(request,c_slug=None):
    c_page=None
    prod_list=None
    if c_slug != None:
        c_page=get_object_or_404(category,slug=c_slug)
        prod_list=product.objects.all().filter(categ=c_page,available=True)
    else:
        prod_list=product.objects.all().filter(available=True)
    paginator=Paginator(prod_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        prod=paginator.page(page)
    except (InvalidPage,EmptyPage):
        prod=paginator.page(paginator.num_pages)
    return render(request,'category.html',{'category':c_page,'product':prod})
def prodetails(request,c_slug,p_slug):
    try:
        p=product.objects.get(categ__slug=c_slug,slug=p_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':p})
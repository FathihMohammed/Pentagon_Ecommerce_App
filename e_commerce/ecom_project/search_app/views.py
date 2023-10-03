from django.shortcuts import render
from django.db.models import Q
from ecom_app.models import product


# Create your views here.
def SearchResult(request):
    products=None
    query=None
    if "q" in request.GET:
        query=request.GET.get("q")
        products=product.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
        return render(request,'search.html',{'query':query,'products':products})
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.views import generic, View

# Create your views here.
from . models import Product
from . forms import ProductForm


class ProductList(generic.ListView):
    template_name = "list.html"
    context_object_name = "items"

    def get_queryset(self):
        return Product.objects.all()[:5]
        # return super().get_queryset()
    

class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.filter(pk=pk).first()
        context = {"item":product}
        return render(request, "templated_detail.html", context=context)


class ProductEdit(View):
    form_class = ProductForm
    initial = {}
    template_name = "templated_edit.html"

    def get(self, request, pk):
        product = Product.objects.filter(pk=pk).first()
        form = self.form_class(initial=product.items())
        context = {"form": form}
        return render(request, self.template_name, context=context)
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
        context = {"form": form}
        
        return render(request, self.template_name, context=context)
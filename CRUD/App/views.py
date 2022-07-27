from django.shortcuts import render
from App.models import Product
from django.http import HttpResponseRedirect

# Home
def home(request):
    all_products = Product.objects.all().order_by('-created_at')
    return render(request, 'home.html', {"products": all_products})

# Add product
def add_product(request):
    if request.method == "POST":
        if request.POST.get('product') \
            and request.POST.get('purchase') \
            and request.POST.get('sale') \
            and request.POST.get('qty') \
            and request.POST.get('gender') \
                or request.POST.get('note'):
            product_new = Product()
            product_new.product = request.POST.get('product')
            product_new.purchase = request.POST.get('purchase')
            product_new.qty = request.POST.get('qty')
            product_new.sale = request.POST.get('sale')
            product_new.gender = request.POST.get('gender')
            product_new.note = request.POST.get('note')
            product_new.save()
            return HttpResponseRedirect('/')
    else:
        return render(request, 'add.html')
# View product


def product(request, product_id):
    product = Product.objects.get(id=product_id)
    if product != None:
        return render(request, 'edit.html', {'product': product})
# Edit Product


def edit_product(request):
    if request.method == "POST":
        product = Product.objects.get(id=request.POST.get('id'))
        if product != None:
            product.product = request.POST.get('product')
            product.purchase = request.POST.get('purchase')
            product.qty = request.POST.get('qty')
            product.sale = request.POST.get('sale')
            product.gender = request.POST.get('gender')
            product.notes = request.POST.get('notes')
            product.save()
            return HttpResponseRedirect('/')

# Delete Product


def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return HttpResponseRedirect('/')

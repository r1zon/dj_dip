from django.shortcuts import render

from phones.models import Product

def add_to_cart(request):
    if 'cart_product' not in request.session.keys():
        request.session['cart_product'] = list()
    # if request.method == 'POST':
    #
    #     if pk not in request.session['reviewed_products']:
    #         form = ReviewForm(request.POST)
    #         if form.is_valid():
    #             request.session['reviewed_products'].append(pk)
    #             request.session.modified = True
    #             print(request.session['reviewed_products'])
    #             Review.objects.create(product_id=pk,
    #                                   name=request.POST.get('name'),
    #                                   text=request.POST.get('text'),
    #                                   rate=request.POST.get('rate'))
    #     return redirect("product_view", pk)

def index(request):
    products = Product.objects.all()
    context = {'tittle': 'index',
               'products': products}
    return render(
        request,
        'index.html',
        context
    )

def cart(request):
    context = {'tittle': 'cart'}
    return render(
        request,
        'cart.html',
        context
    )
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect

from phones.models import Product, Order, ProductCounts, Article, ProductType


def add_to_cart(request):
    if 'cart' not in request.session.keys():
        request.session['cart'] = list()
    if request.method == 'POST' and 'id' in request.POST:
        id = request.POST.get('id')
        if list(filter(lambda product: product['id'] == id, request.session['cart'])) == []:
            prod_dict = {'id': id,
                         'name': Product.objects.get(pk=id).name,
                         'count': 1}
            request.session['cart'].append(prod_dict)
            request.session.modified = True
        else:
            for prod in request.session['cart']:
                if prod['id'] == id:
                    count = 1 + prod['count']
                    prod['count'] = count
                    request.session.modified = True
    if request.user.is_authenticated:
        if request.method == 'POST' and 'id' in request.POST:
            order = Order.objects.get_or_create(user=request.user, is_ordered = False)
            print(order)
            # if order[0].is_ordered == True:
            #     order = Order.objects.create(user=request.user)
            # else:
            for product in request.session['cart']:
                if list(order[0].products.all().filter(id=product['id'])) != []:
                    order[0].product_counts.all().filter(product=product['id']).update(count = product['count'])
                else:
                    order[0].products.add(product['id'], through_defaults={'count': product['count']})

def cart(request):
    if request.user.is_authenticated:
        try:
            cart = Order.objects.get(user=request.user, is_ordered=False)
            cart = cart.product_counts.all()
        # print(cart.product_counts.all())
        # for product in cart.product_counts.all():
        #     print(type(product.product.name), '+', type(product.count))
            total_count = 0
            for product in cart:
                total_count += product.count
        except:
            cart = []
            total_count = 0
        context = {'tittle': 'cart',
                   'cart': cart,
                   'total_count': total_count}
    elif 'cart' not in request.session.keys():
        pass
    else:
        cart = request.session['cart']
        total_count = 0
        for product in cart:
            total_count += product['count']
        context = {'tittle': 'cart',
                   'cart': cart,
                   'total_count': total_count}
    try:
        if request.method == 'POST' and 'cart' in request.POST:
            order = Order.objects.get(user=request.user, is_ordered=False)
            order.is_ordered = True
            order.save()
            request.session['cart'] = []
            return redirect("index")
    except:
        return redirect("cart")
    return render(
        request,
        'cart.html',
        context
    )

def index(request):
    products = Product.objects.all()
    articles = Article.objects.all()
    products_type = ProductType.objects.all()
    type = request.GET.get('type')
    sub_type = request.GET.get('subtype')
    if type:
        objects = Product.objects.filter(product_type__name = sub_type)
        context = {'tittle': sub_type,
                   'products_type': products_type,
                   'types': type
                   }
        if list(objects) == []:
            return render(
                request,
                'empty_section.html',
                context
            )
        else:
            paginator = Paginator(objects, 1)
            page = request.GET.get('page')
            try:
                products = paginator.page(page)
            except PageNotAnInteger:
                products = paginator.page(1)
            except EmptyPage:
                products = paginator.page(paginator.num_pages)
            context = {'products': products,
                       'tittle': sub_type,
                       'types': type,
                       'page': page,
                       'products_type': products_type
                       }
            add_to_cart(request)
            return render(
                request,
                'smartphones.html',
                context
            )
    context = {'tittle': 'index',
               'products': products,
               'articles': articles,
               'products_type': products_type
               }
    add_to_cart(request)
    return render(
        request,
        'index.html',
        context
    )


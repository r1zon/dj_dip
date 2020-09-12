from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect

from main.views import add_to_cart
from phones.forms import ReviewForm
from phones.models import Product, Review


def smartphones(request):
    objects = Product.objects.filter(product_type__product_type='phone')
    context = {'tittle': 'smartphones',
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
                   'tittle': 'smartphones',
                   'page': page
                   }
        add_to_cart(request)
        return render(
            request,
            'smartphones.html',
            context
        )

def tablets(request):
    objects = Product.objects.filter(product_type__product_type='tablet')
    context = {'tittle': 'smartphones',
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
                   'tittle': 'smartphones',
                   'page': page
                   }
        add_to_cart(request)
        return render(
            request,
            'tablets.html',
            context
        )

def accessories(request):
    objects = Product.objects.filter(product_type__product_type='acc')
    context = {'tittle': 'accessories',
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
                   'tittle': 'accessories',
                   'page': page
                   }
        add_to_cart(request)
        return render(
            request,
            'accessories.html',
            context
        )

def empty(request):
    context = {'tittle': 'accessories'}
    return render(
        request,
        'empty_section.html',
        context
    )

def product_view(request, slug):
    print(slug)
    product = get_object_or_404(Product, slug=slug)
    pk = product.id
    template = 'product.html'
    if product.product_type == 'acc':
        title = 'accessories'
    else:
        title = 'smartphones'
    context = {'product': product,
               'tittle': title,
               'form': ReviewForm()}
    add_to_cart(request)
    if 'reviewed_products' not in request.session.keys():
        request.session['reviewed_products'] = list()
    if request.method == 'POST' and 'review' in request.POST:
        if pk not in request.session['reviewed_products']:
            form = ReviewForm(request.POST)
            if form.is_valid():
                request.session['reviewed_products'].append(pk)
                request.session.modified = True
                print(request.session['reviewed_products'])
                Review.objects.create(product_id=pk,
                                      name=request.POST.get('name'),
                                      text=request.POST.get('text'),
                                      rate=request.POST.get('rate'))
        return redirect("product_view", pk)
    reviews = Review.objects.all().filter(product_id=pk)
    context.update({'reviews': reviews})
    if pk in request.session['reviewed_products']:
        context.update({'is_review_exist': request.session})
    return render(request, template, context)
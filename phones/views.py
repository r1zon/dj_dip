from urllib.parse import urlencode

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect

from phones.forms import ReviewForm
from phones.models import Product, Review


def smartphones(request):
    objects = Product.objects.all()
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
    return render(
        request,
        'smartphones.html',
        context
    )
def empty(request):
    context = {'tittle': 'accessories'}
    return render(
        request,
        'empty_section.html',
        context
    )

def product_view(request, pk):
    template = 'phone.html'
    product = get_object_or_404(Product, id=pk)
    context = {'product': product,
               'tittle': 'smartphones',
               'form': ReviewForm()}
    if 'reviewed_products' not in request.session.keys():
        request.session['reviewed_products'] = list()
    if request.method == 'POST':
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
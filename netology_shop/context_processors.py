from phones.models import ProductType, SubProductType


def category(request):
    return {'types': ProductType.objects.all(),
            'sub_types': SubProductType.objects.all()}

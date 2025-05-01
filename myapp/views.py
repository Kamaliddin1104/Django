from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.models import Group
from datetime import datetime
from .models import Product


def myapp_page(request: HttpRequest):
    
    context = {
        "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    return render(request, 'myapp/main.html', context=context)




def groups_list_page(request: HttpRequest):
    context = {
        'groups': Group.objects.prefetch_related('permissions').all(),
    }
    return render(request, 'myapp/groups_list.html', context=context)



def products_page(request: HttpRequest):
    context = {
        'table_of_products': Product.objects.all(),
    }
    return render(request, 'myapp/products_db.html', context=context)













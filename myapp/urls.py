from django.urls import path
from .views import groups_list_page, products_page, myapp_page
from .views import orders


# myapp/urls


urlpatterns = [
    path('', myapp_page, name='index'), # myapp/
    path('groups/', groups_list_page, name='groups-list'), # myapp/groups/
    path('products/', products_page, name='products-list'), # myapp/products/
    path('orders/', orders, name='orders'), # myapp/orders/
]
from django.contrib import admin
from .models import Product, Orders


class OrdersInline(admin.StackedInline): # Встраиваемая orders_product для отображения в админке
    model = Orders.products.through
    extra = 1 # Количество дополнительных полей для добавления в админке


@admin.register(Product) # Регистрация модели в админке
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        OrdersInline, # Добавление колонок для редактирования связанных заказов
    ]
    list_display = ('id', 'name', 'short_description', 'price', 'discount', 'created_at') # Определяем поля, которые будут отображаться в админке
    list_display_links = 'id', 'name' # Определяем поля, которые будут ссылками на редактирование
    ordering = ('id',) # Определяем порядок сортировки
    search_fields = ('name', 'descriptions') # Добавляем поле поиска обьектов в админке
    
    def short_description(self, obj: Product):
        return obj.descriptions if len(obj.descriptions) < 48 else obj.descriptions[:48] + '...'
    
    
    
class ProductInline(admin.StackedInline): # Встраиваемая orders_product для отображения в админке
    model = Orders.products.through # Указываем связь между моделями
    extra = 1 # Количество дополнительных полей для добавления в админке
    
    

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline, # Встраиваемая модель для отображения в админке
    ]
    list_display = ('id', 'delivery_address', 'promocode', 'created_at', 'user_verbose')
    list_display_links = ('id', 'delivery_address')
    ordering = ('id',)
    search_fields = ('delivery_address',)
    
    def get_queryset(self, request):
        return Orders.objects.select_related('user') # Оптимизация запросов к базе данных, чтобы избежать N+1 проблемы

    
    def user_verbose(Self, obj: Orders):
        return obj.user.first_name or obj.user.username # Если у пользователя есть имя, то выводим его, иначе выводим юзернейм
    
    
    
    
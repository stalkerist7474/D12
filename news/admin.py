from msilib.schema import Class
from django.contrib import admin
from .models import Author, Category, Post, Comment, Subscriber


 
# создаём новый класс для представления товаров в админке
class newsAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('post_type', 'post_author', 'post_date_created', ) # оставляем только имя и цену товара
    list_filter = ('category', 'post_author', 'post_type') # добавляем примитивные фильтры в нашу админку
    search_fields = ('post_type', 'category__name','post_author') # тут всё очень похоже на фильтры из запросов в базу, давайте 
    
 
 
# Register your models here.






admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, newsAdmin)
admin.site.register(Comment)
admin.site.register(Subscriber)

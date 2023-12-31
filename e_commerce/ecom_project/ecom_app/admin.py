from django.contrib import admin
from .models import category,product
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category,CategoryAdmin)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','stock','available','created','update']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(product,ProductAdmin)
from django.contrib import admin
from merchant.models import Product,Celerytime
# Register your models here.


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price', 'amount') 
    search_fields = ('name',)

class CelerycreatetimeAdmin(admin.ModelAdmin):
	list_display = ('name','Celery_createtime',)

admin.site.register(Celerytime, CelerycreatetimeAdmin)


admin.site.register(Product,ProductAdmin)


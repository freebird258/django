from django.contrib import admin
from merchant.models import Product,Contact,Tag
# Register your models here.


# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag
class ContactAdmin(admin.ModelAdmin):
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',),
            'fields': ('age',),
        }]
 
    )

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price', 'amount') 
    search_fields = ('name',)

admin.site.register(Contact, ContactAdmin)


admin.site.register(Product,ProductAdmin)


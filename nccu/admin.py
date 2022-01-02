from django.contrib import admin

from .models import Customer, Activity, Remaining, Product,Manufacture_Order,Material
# Register your models here.
admin.site.register(Product)
admin.site.register(Manufacture_Order)
admin.site.register(Material)
admin.site.register(Activity)
admin.site.register(Customer)
admin.site.register(Remaining)



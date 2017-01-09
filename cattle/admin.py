from django.contrib import admin

# Register your models here.
from .models import Sale_Bill, Buyer, Seller, Brand, Description, Purchase

admin.site.register(Buyer)
admin.site.register(Seller)
admin.site.register(Brand)
admin.site.register(Description)
admin.site.register(Sale_Bill)
admin.site.register(Purchase)

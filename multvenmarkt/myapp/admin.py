from django.contrib import admin

from django.contrib import admin
from .models import (
    Customer,
    Product,
    Category,
    Product_Category,
    Vendor,
    Maintenance_Service,
    Order,
    Order_Item,
    Vendor_Billing,
    Service_Reviews,
    Reviews_Product,
    Reviews_vendors,
    Offer,
    Subscription,
)


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Product_Category)
admin.site.register(Vendor)
admin.site.register(Maintenance_Service)
admin.site.register(Order)
admin.site.register(Order_Item)
admin.site.register(Vendor_Billing)
admin.site.register(Service_Reviews)
admin.site.register(Reviews_Product)
admin.site.register(Reviews_vendors)
admin.site.register(Offer)
admin.site.register(Subscription)
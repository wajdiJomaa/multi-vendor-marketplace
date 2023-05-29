from django.db import models
from django.contrib.auth.models import User

class UserDjango(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    adresse = models.CharField(max_length=255)

class Product(models.Model):
    Vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    ProductName = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    MadeIn = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    additionalInfos = models.CharField(max_length=255)
    Description = models.TextField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.CharField(max_length=255)
    Availability = models.BooleanField()

class Category(models.Model):
    CategoryName = models.CharField(max_length=255)

class Product_Category(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Description = models.TextField()
    ContactPerson = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    PhoneNumber = models.CharField(max_length=20)

class Maintenance_Service(models.Model):
    Vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    ServiceName = models.CharField(max_length=255)
    Description = models.TextField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)

class Order(models.Model):
    Vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    OrderDate = models.DateField()
    Status = models.CharField(max_length=255)
    description = models.TextField()

class Order_Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    RoundedPrice = models.DecimalField(max_digits=10, decimal_places=2)

class Vendor_Billing(models.Model):
    Vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    Order = models.ForeignKey(Order, on_delete=models.CASCADE)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    BillingDate = models.DateField()

class Service_Reviews(models.Model):
    Service = models.ForeignKey(Maintenance_Service, on_delete=models.CASCADE)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Rating = models.IntegerField()
    Review_Text = models.TextField()
    Review_Date = models.DateField()

class Reviews_Product(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Rating = models.IntegerField()
    Review_Text = models.TextField()
    Review_Date = models.DateField()

class Reviews_vendors(models.Model):
    Vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Rating = models.IntegerField()
    Review_Text = models.TextField()
    Review_Date = models.DateField()

class Offer(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

class Subscription(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    subscription_date = models.DateField()

# Create your models here.

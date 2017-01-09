from django.db import models
from django.utils import timezone


class Buyer(models.Model):
    brand = models.CharField(max_length=30)
    address = models.CharField(max_length=200)

class Seller(models.Model):
    brand = models.CharField(max_length=30)
    address = models.CharField(max_length=200)

class Brand(models.Model):
    name = models.CharField(max_length=15)

class Description(models.Model):
    short = models.CharField(max_length=15)
    long = models.CharField(max_length=100)

class Sale_Bill(models.Model):
    creator = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(default=timezone.now)
    buyer_brand = models.ForeignKey('Buyer')
    buyer_agent = models.CharField(max_length=100)
    total_head = models.PositiveIntegerField(editable=False, blank=True, null=True)
    total_weight = models.DecimalField(decimal_places=2, max_digits=8, editable=False, blank=True, null=True)
    avg_weight = models.DecimalField(decimal_places=2, max_digits=8, editable=False, blank=True, null=True)
    gross_total = models.DecimalField(decimal_places=2, max_digits=10, editable=False, blank=True, null=True)
    avg_price = models.DecimalField(decimal_places=2, max_digits=10, editable=False, blank=True, null=True)
    commission = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    feed = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    freight = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    other = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    total = models.DecimalField(decimal_places=2, max_digits=10, editable=False, blank=True, null=True)

class Purchase(models.Model):
    bill = models.ForeignKey('Sale_Bill')
    seller = models.ForeignKey('Seller')
    no_head = models.PositiveSmallIntegerField()
    description = models.ForeignKey('Description')
    tag_no = models.PositiveIntegerField()
    pen_no = models.PositiveSmallIntegerField()
    brand = models.ForeignKey('Brand')
    weight = models.DecimalField(decimal_places=2, max_digits=8)
    price_cwt = models.DecimalField(decimal_places=2, max_digits=8)
    price_head = models.DecimalField(decimal_places=2, max_digits=8, blank=True, null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=8)

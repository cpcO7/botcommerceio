from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model, CharField, BooleanField, ForeignKey, CASCADE


class Currency(Model):
    name = CharField(max_length=255)


class Shop(Model):
    name = CharField(max_length=255)


class CategoryHead(Model):
    name = CharField(max_length=255)


class Category(Model):
    emoji_status = CharField(max_length=255)
    name = CharField(max_length=255)
    parent_category = ForeignKey('users.CategoryHead', CASCADE)
    availability = BooleanField()
    show_in_website = BooleanField()


class ShopCategory(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ShopProduct(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    weight = models.FloatField()
    height = models.FloatField()
    length = models.FloatField()
    width = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    name = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Savat(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    price = models.FloatField()
    paid = models.BooleanField(default=False)

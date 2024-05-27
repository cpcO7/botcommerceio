from django.contrib import admin
from django.contrib.auth.models import Group,User

from .models import Category, Product
admin.site.register(Category)
admin.site.register(Product)


admin.site.unregister(Group)
admin.site.unregister(User)

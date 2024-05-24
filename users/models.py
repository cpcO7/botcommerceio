from django.db.models import Model, CharField, BooleanField, ForeignKey, CASCADE


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

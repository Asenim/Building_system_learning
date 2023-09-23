from django.db import models


# Create your models here.
class ProductOwner(models.Model):
    owner_name = models.TextField(max_length=100, null=False)


class Product(models.Model):
    product_name = models.TextField(max_length=100, null=False)
    product_owner = models.ForeignKey(ProductOwner, on_delete=models.CASCADE, null=False)


class User(models.Model):
    user_name = models.TextField(max_length=100, null=False)
    access_product = models.ManyToManyField(Product, through='AccessesProductsUsers')


class AccessesProductsUsers(models.Model):
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)


class Lesson(models.Model):
    lesson_name = models.TextField(max_length=100, null=False)
    link_to_video = models.TextField(max_length=300, null=False)
    video_duration = models.IntegerField(null=False)
    belongs_to_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    viewing_user = models.ManyToManyField(User, through='LessonViewingTime')


class LessonViewingTime(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    viewed_time = models.IntegerField(default=0, null=False)
    status = models.TextField(default='Not viewed', null=False)

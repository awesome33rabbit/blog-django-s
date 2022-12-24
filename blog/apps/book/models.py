from django.db import models

from user.models import User


# Create your models here.
class Book(models.Model):
    name = models.CharField("书名", max_length=32)
    desc = models.CharField("描述", max_length=128)

    # book = models.ForeignKey(Book, on_delete=models.CASCADE)
    price = models.FloatField("价格", default=0)
    count = models.IntegerField("库存", default=0)


class Sale(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    count = models.IntegerField("数量")


class Borrow(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    count = models.IntegerField("数量")

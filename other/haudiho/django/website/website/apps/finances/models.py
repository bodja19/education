import datetime
from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone


class People(models.Model):
    debtor = models.ForeignKey(User, on_delete=models.CASCADE)
    debtor_name = models.CharField("Name debtor", max_length=50)

    def __str__(self):
        return self.debtor_name



class MyMoney(models.Model):
    # my money гроші які мені винні

    money_id = models.ForeignKey(People, on_delete=models.CASCADE)
    suma = models.DecimalField('Suma', max_digits=8, decimal_places=2)
    comment_text = models.CharField("Text comment", max_length=200)
    calculation = models.BooleanField()
    pub_date = models.DateTimeField('Date publication')

    def __str__(self):
        suma = str(self.suma)
        return suma

class NotMyMoney(models.Model):
    # not my money гроші які я винний

    money_id = models.ForeignKey(People, on_delete=models.CASCADE)
    suma = models.DecimalField('Suma', max_digits=8, decimal_places=2)
    comment_text = models.CharField("Text comment", max_length=200)
    calculation = models.BooleanField()
    pub_date = models.DateTimeField('Date publication')

    def __str__(self):
        suma = str(self.suma)
        return suma

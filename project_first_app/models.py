from django.db import models


class Car(models.Model):
    number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)


class Owner(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    birth_date = models.DateTimeField()
    ownerships = models.ManyToManyField(Car, through='Ownership')


class License(models.Model):
    owner_license = models.ForeignKey(Owner, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date = models.DateField()


class Ownership(models.Model):
    ownerships = models.ForeignKey(Owner, on_delete=models.CASCADE)
    carownership = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start = models.DateTimeField()
    date_ending = models.DateTimeField()

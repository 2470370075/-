from django.db import models
import django.utils.timezone as timezone
from django.contrib import auth
import datetime

class Us(models.Model):

    id=models.AutoField(primary_key=True)
    name=models.CharField(null=False,max_length=20,unique=True)
    password=models.CharField(null=False,max_length=20)


class Userinfo(models.Model):

    id=models.AutoField(primary_key=True)
    name=models.CharField(null=False,max_length=20,unique=True)
    password=models.CharField(null=False,max_length=20)

class City(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=10)


class Publish(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(null=False,max_length=20)


class Book(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(null=False,max_length=20)
    kucun=models.IntegerField(default=100)
    maichu=models.IntegerField(default=10)
    price=models.DecimalField(max_digits=5,decimal_places=2,default=20.00)
    pid=models.ForeignKey(to=Publish)
    def __str__(self):
        return "<Book Object: {}>".format(self.name)


class Author(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(null=False,max_length=20)
    book=models.ManyToManyField(to=Book)
    birthday = models.DateField(default=timezone.now)
    def __str__(self):
        return self.name




class Author2(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(null=False,max_length=20)
    dept=models.IntegerField(default=1)
    info = models.OneToOneField(to='Info')

class Info(models.Model):
    addr=models.CharField(null=False,max_length=20)
    hobby=models.CharField(null=False,max_length=20)
    price=models.IntegerField(default=1000)


class Author22222222222222222222(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(null=False,max_length=20)
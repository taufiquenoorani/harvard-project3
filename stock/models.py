from django.db import models

class Size(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('id',)

class PizzaType(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('id',)

class Extra(models.Model):
    name = models.CharField(max_length = 50)
    Sizes = models.ForeignKey(Size, on_delete = models.CASCADE)
    price = models.FloatField()
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('id',)

class Topping(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField(default= 1)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('id',)

class Salad(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('id',)

class Sub(models.Model):
    name = models.CharField(max_length=30)
    Sizes = models.ForeignKey(Size, on_delete = models.CASCADE)
    price = models.FloatField()
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('id',)

class Pasta(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('id',)

class Pizza(models.Model):
    name = models.CharField(max_length=30)
    Toppings = models.IntegerField()
    PizzaTypes = models.ForeignKey(PizzaType, on_delete = models.CASCADE, null = True)
    Sizes = models.ForeignKey(Size, on_delete = models.CASCADE)
    price = models.FloatField()
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('id',)

class DinnerPlatter(models.Model):
    name = models.CharField(max_length=30)
    Sizes = models.ForeignKey(Size, on_delete = models.CASCADE)
    price = models.FloatField()
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('id',)
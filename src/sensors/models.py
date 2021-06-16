from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


STATUS_CHOICE = {
    'ON':  1
    'OFF': 0
}



class Sensors(models.Model):
    name = models.CharField(max_length=210, verbose_name='Nombre')
    date = models.DateTimeField(auto_now_add=True)
    mac_addres = models.TextField(max_length=50, verbose_name="MAC")
    voltaje = 


    def __str__(self):
        return str(self.name)


class SensorDHT11Temp:
    pass


class SensorDHT22Temp:
    pass


class GraficaSensor:
    sensor = models.ForeignKey(Sensors, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    time = models.DateTimeField(default=timezone.now)
    status = models.Model(STATUS_CHOICE='ON')
    datos =  models.Model(temp().context)


"""class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField(blank=True)
    salesman = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.total_price = self.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return "Concepto: {} - Cantidad: {} - Total: {}".format(self.product.name, self.quantity, self.total_price)"""


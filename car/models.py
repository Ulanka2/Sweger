from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Car(models.Model):
    class StatusType(models.TextChoices):
        REGISTRATION = 'registration'
        LVL1 = ' LVL1'
        LVL2 = ' LVL2'
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', null=True)
    year_issue = models.IntegerField(default=2010)
    maker = models.CharField(max_length=255)
    coutry = models.CharField(max_length=128)
    worker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='worker', null=True)

    

class CarDocument(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car', null=True)
    file = models.FileField()
    status = models.CharField(max_length=50)


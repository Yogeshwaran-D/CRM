from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Agent(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user}"

class Leads(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    age=models.IntegerField()
    agent=models.ForeignKey(Agent,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural="Leads"

    def __str__(self) :
        return f"{self.first_name} {self.last_name}"
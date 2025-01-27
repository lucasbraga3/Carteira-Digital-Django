from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserWallet(AbstractUser):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return f"carteira de {self.user.username}"

class Transaction(models.Model):
    recipiente = models.ForeignKey(UserWallet, on_delete=models.PROTECT,blank=False)
    destinatario = models.ForeignKey(UserWallet, on_delete=models.PROTECT,blank=False)
    quantidade =  models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"usuario {self.recipiente.user.username} enviOU ${self.quantidade} para {self.destinatario.user.username}"
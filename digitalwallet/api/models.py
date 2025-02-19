from django.db import models
from django.contrib.auth.models import AbstractUser, User
# Create your models here.

class UserWallet(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="wallet")
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return f"carteira de {self.user.username}"

class Transaction(models.Model):
    recipiente = models.ForeignKey(UserWallet, on_delete=models.PROTECT,blank=False, related_name="recieved_transaction")
    destinatario = models.ForeignKey(UserWallet, on_delete=models.PROTECT,blank=False, related_name="sent_transaction")
    quantidade =  models.DecimalField(max_digits=10, decimal_places=2)
    related_name = "transacoes"
    def __str__(self):
        return f"usuario {self.recipiente.user.username} enviOU ${self.quantidade} para {self.destinatario.user.username}"
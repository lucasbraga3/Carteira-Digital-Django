from rest_framework import serializers
from .models import UserWallet, Transaction

class UserWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model: UserWallet
        fields: '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model: Transaction
        fields: '__all__'
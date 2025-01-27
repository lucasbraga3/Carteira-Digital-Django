from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.db import transaction
from models import UserWallet, Transaction
from serializers import UserWalletSerializer, TransactionSerializer
# Create your views here.

class DetalhesWalletView(APIView):
    permission_classes = [IsAuthenticated]

    def get_walletdetes(self, req):
        wallet = req.user.wallet
        serializer = UserWalletSerializer(wallet)
        return Response(serializer.data)

class TransferView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, req):
        quantia = req.data.get('quantia')
        if not quantia or quantia<=0:
            return Response({'erro':'quantia invalida'},status=status.HTTP_400_BAD_REQUEST)
        
        user_wallet = req.user.wallet
        recipient_wallet = req.user.recipent
        try:
            with transaction.atomic():
                wallets = UserWallet.object.select_for_update().filter(id__in=[user_wallet.id,recipient_wallet.id])
                user_wallet, recipient_wallet = wallets[0],wallets[1]
                user_wallet.saldo -= quantia
                recipient_wallet += quantia
                user_wallet.save()
                recipient_wallet.save()
                Transaction.objects.create(
                    recipiente = recipient_wallet,
                    destinatario = user_wallet,
                    quantia = quantia
                )

                return Response({'message':'transacao realizada com sucesso'})
        except Exception:
            return Response({'error':str(Exception)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
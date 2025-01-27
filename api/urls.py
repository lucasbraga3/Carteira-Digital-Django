from django.urls import path
from .views import DetalhesWalletView, TransferView

urlpatterns = [
    path('carteira/', DetalhesWalletView.as_view(),name='MinhaCarteira'),
    path('/tranferir', TransferView.as_view(),name='Tranferencia' )
]
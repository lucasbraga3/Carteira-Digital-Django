import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from api.models import Wallet, Transaction
from faker import Faker
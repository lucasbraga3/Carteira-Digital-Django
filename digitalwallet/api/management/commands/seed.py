import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from api.models import UserWallet, Transaction
from faker import Faker

fake = Faker()

class Command(BaseCommand):
    help = 'Seeds the database with mock data'

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding data...")

        # Create mock users and wallets
        for _ in range(10):  # Create 10 users
            first_name = fake.first_name()
            last_name = fake.last_name()
            username = f"{first_name.lower()}_{last_name.lower()}"
            email = fake.email()
            password = "password123"  # Use a default password for testing

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )

            # Create a wallet for the user
            UserWallet.objects.create(user=user, saldo=random.randint(100, 10000))

        self.stdout.write("Created 10 users and wallets.")

        # Create mock transactions
        wallets = UserWallet.objects.all()
        for _ in range(50):  # Create 50 transactions
            from_wallet = random.choice(wallets)
            to_wallet = random.choice(wallets.exclude(id=from_wallet.id))
            amount = random.randint(10, 1000)
            Transaction.objects.create(
                recipiente=from_wallet,
                destinatario=to_wallet,
                quantidade=amount,
            )

        self.stdout.write("Created 50 transactions.")

        self.stdout.write(self.style.SUCCESS("Data seeding complete!"))
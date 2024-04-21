from django.db import models

# Create your models here.
class Wallet(models.Model):
    label = models.CharField(
        max_length=255,
        help_text="The Unique Identifier for the Wallet"
    )

    amount = models.FloatField(
        default=0
    )

class Transaction(models.Model):
    wallet = models.ForeignKey(
        Wallet,
        on_delete=models.CASCADE
    )

    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"

    type_choices = [
        (DEPOSIT, "deposit"),
        (WITHDRAWAL, "withdrawal")
    ]

    type = models.CharField(
        max_length=10,
        choices=type_choices,
    )

    timestamp = models.DateTimeField()

    description = models.CharField(
        max_length=255
    )

    amount = models.FloatField(
        default=0
    )

    def __str__(self):
        return self.description
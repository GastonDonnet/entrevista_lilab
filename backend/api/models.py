from django.db import models
import random


class Client(models.Model):
    class Punctuation(models.TextChoices):
        BUENO = 'B', ('Bueno')
        MALO = 'M', ('Malo')
        REGULAR = 'R', ('Regular')

    name = models.CharField(max_length=100)
    total_debt = models.FloatField()
    punctuation = models.CharField(
        max_length=1,
        choices=Punctuation.choices,
        default=Punctuation.REGULAR,
    )

    def __str__(self):
        return f'{self.id} - {self.name} - {self.punctuation} - {self.total_debt}'


class Credit(models.Model):
    class State(models.TextChoices):
        NO_REVISADO = 'NR', ('No revisado')
        APROBADO = 'A', ('Aprobado')
        NO_APROBADO = 'NA', ('No aprobado')

    class PaymentState(models.TextChoices):
        PAGADA = 'P', ('Pagada')
        NO_PAGADA = 'NP', ('No pagada')

    amount = models.FloatField()
    state = models.CharField(
        max_length=2,
        choices=State.choices,
        default=State.NO_REVISADO,
    )
    payment_state = models.CharField(
        max_length=2,
        choices=PaymentState.choices,
        default=PaymentState.NO_PAGADA,
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def get_ia_evaluation(self):

        punctuation = 10
        punctuation *= max(0.5, 1-self.amount/50000)

        # Ajuste por puntuación del cliente
        if self.client.punctuation == "M":
            punctuation *= 0.4
        elif self.client.punctuation == "R":
            punctuation *= 0.8

        punctuation = round(punctuation)

        if punctuation > 10:
            punctuation = 10
        elif punctuation < 1:
            punctuation = 1

        return punctuation

    def __str__(self):
        return f'{self.id} - {self.state} - {self.payment_state}'




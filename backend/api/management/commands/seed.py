# <project>/<app>/management/commands/seed.py
from django.core.management.base import BaseCommand
import random
from api.models import Client, Credit

# python manage.py seed --mode=refresh

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    Client.objects.all().delete()
    Credit.objects.all().delete()


def create_client():
    first_names = ["Gastón", "Juan", "Sebastian", "Pedro", "Julian", "Martin"]
    last_names = ["Donnet", "Martinez", "Fabro", "Zamora", "Batalla"]
    punctuation = ["B", "R", "M"]

    client = Client(
        name=random.choice(first_names) + " " + random.choice(last_names),
        total_debt=round(random.random()*100000, 2),
        punctuation=random.choice(punctuation)
    )
    client.save()
    return client


def create_credit(clients):

    states = ["NR", "A", "NP"]
    payment_states = ["NP", "P"]

    credit = Credit(
        amount=round(random.random()*100000, 2),
        state=random.choice(states),
        payment_state=random.choice(payment_states),
        client=random.choice(clients)
    )
    credit.save()
    return credit


def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    # Creating 20 clients
    for i in range(20):
        create_client()

    clients = Client.objects.all()
    for i in range(200):
        create_credit(clients)

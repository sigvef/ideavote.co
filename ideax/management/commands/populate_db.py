from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from faker import Factory as FakeFactory
from ideax.idea.models import Idea
import random


class Command(BaseCommand):
    help = 'Seed database with randomly generated data.'

    def handle(self, *args, **options):
        fake = FakeFactory.create()

        users = []

        print 'generating 1000 users'
        for _ in range(1000):
            name = fake.name()
            user = get_user_model().objects.create_user(name)
            users.append(user)

        for i in range(100):
            print 'generating idea', i
            idea = Idea.objects.create(
                slug_id=random.randint(1, 9999999999),
                title=fake.text()[:random.randint(0, 256)],
                text=fake.text(),
                author=random.choice(users))
            shuffled = users[:]
            random.shuffle(shuffled)
            voters = shuffled[:random.randint(0, len(users))]
            idea.upvoters.add(*voters)

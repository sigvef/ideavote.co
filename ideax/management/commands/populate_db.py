from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Factory as FakeFactory
from ideax.idea.models import Idea
from ideax.comment.models import Comment
import datetime
import random


class Command(BaseCommand):
    help = 'Seed database with randomly generated data.'

    def handle(self, *args, **options):
        fake = FakeFactory.create()

        users = []

        print 'generating 100 users'
        for _ in range(100):
            name = fake.name()
            user = get_user_model().objects.create_user(name)
            users.append(user)

        ideas = []
        for i in range(30):
            print 'generating idea', i
            created_at = timezone.now() - datetime.timedelta(
                seconds=random.randint(0, 999999))
            idea = Idea.objects.create(
                slug_id=random.randint(1, 9999999999),
                title=fake.text()[:random.randint(0, 256)],
                text=fake.text(),
                author=random.choice(users),
                created_at=created_at,
                updated_at=created_at)
            ideas.append(idea)
            shuffled = users[:]
            random.shuffle(shuffled)
            voters = shuffled[:random.randint(0, len(users))]
            idea.upvoters.add(*voters)

        print 'generating 1000 comments'
        comments = []
        first = True
        for i in range(1000):
            if i % 100 == 0:
                print 'comment %s...' % i
            author = random.choice(users)
            text = fake.text()
            comment = Comment.objects.create(
                author=author.username,
                text=text)
            if first or random.random() < 0.1:
                comment.idea = random.choice(ideas)
                comment.save()
                first = False
            else:
                parent = random.choice(comments)
                comment.parent = parent
                comment.idea = parent.idea
                comment.save()
            comments.append(comment)
            idea = comment.idea
            idea.comment_count = idea.comment_count + 1
            idea.save()

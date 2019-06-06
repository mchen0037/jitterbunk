import django
django.setup()

from bunk.models import Bunk
from django.contrib.auth.models import User
from django.utils import timezone


import random

for i in range(10000):
    people = random.sample(set(User.objects.all()),2)
    b = Bunk(
            from_user = people[0],
            to_user = people[1],
            time = timezone.now()
        )
    b.save()

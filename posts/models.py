from django.db import models
from django.utils import timezone
import uuid
from django.contrib.auth.models import User
from django.conf import settings

class Post(models.Model):
    post_id = models.UUIDField(default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    TAGS = [
    ('FB', 'Football'),
    ('RD', 'Rides'),
    ('TE', 'Tech'),
]
    category = models.CharField(
        max_length=2,
        choices=TAGS,
    )

    def __str__(self):
        return f'{self.title} written by {self.author.username}'

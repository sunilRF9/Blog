from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone
import uuid
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Post(models.Model):
    post_id = models.UUIDField(default=uuid.uuid4, editable=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    overview = models.TextField()
    content = HTMLField()
    comments = models.IntegerField(default=0)
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(null=True, blank=True)
    category = models.ManyToManyField(Category)
    featured = models.BooleanField()
    previous_post = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='previous')
    next_post = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='next')

    def __str__(self):
        return f'{self.title}' 

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'id':self.id})

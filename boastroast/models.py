from django.db import models

class Post(models.Model):
    Boast = 'Boast'
    Roast = 'Roast'

    POST_CHOICES = [
        (Boast, 'Boast'),
        (Roast, 'Roast')
    ]

    body = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    type_of_post = models.CharField(choices=POST_CHOICES, default=Boast, max_length=5)

    def __str__(self):
        return self.body
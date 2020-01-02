from django.db import models
import computed_property


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
    score = computed_property.ComputedIntegerField(compute_from='get_score')

    @property
    def get_score(self):
        vote_score = self.upvotes - self.downvotes
        return vote_score
 

    def __str__(self):
        return self.body

def magicString():
    character = string.ascii_lower

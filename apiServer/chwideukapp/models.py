from django.db import models


class ChwideukModel(models.Model):
    title = models.CharField(max_length=70, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
from django.db import models


class flow(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='post/')
    create_at = models.DateTimeField(auto_now_add=True)

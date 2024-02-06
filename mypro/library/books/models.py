from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    price=models.IntegerField()
    def __str__(self):
        return f"{self.title} by {self.author}"

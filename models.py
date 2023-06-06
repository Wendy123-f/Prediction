from django.db import models

# Create your models here.
class Plagiarism(models.Model):
    text = models.TextField(max_length=1000)

    def __str__(self):
        return self.text
    
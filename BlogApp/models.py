from django.db import models

# Create your models here.

class writing(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.text[:100]
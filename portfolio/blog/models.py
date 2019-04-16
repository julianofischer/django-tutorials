from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[0:100]+"..."

    def __str__(self):
        return self.title

from django.db import models
import os

# Create your models here.
class Documento(models.Model):
    titulo = models.TextField()
    upload = models.FileField(upload_to='uploads/')
    thumb = models.ImageField(upload_to="uploads/", editable=False, null=True)

    def __str__(self):
        return self.titulo


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files import File

@receiver(post_save, sender=Documento)
def make_thumbnail(sender, instance, **kwargs):
    # convert -density 150 wellinton.pdf[0] -quality 90 -flatten
    # -scale 20% output.png
    path = instance.upload.path
    img_path = path[:-3]+"png"
    cmd = f'convert -density 150 {path}[0] -quality 90 -flatten -scale 20% {img_path}'
    os.system(cmd)
    image_file = open(img_path, "rb")
    django_file = File(image_file)
    post_save.disconnect(make_thumbnail, sender=sender)
    instance.thumb.save(os.path.basename(img_path), django_file, save=True)
    post_save.connect(make_thumbnail, sender=sender)
    return True

    def save(self, stop=False, *args, **kwargs):
        super(Documento, self).save(*args, **kwargs)

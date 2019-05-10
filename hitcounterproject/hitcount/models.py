from django.db import models, transaction
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
# Create your models here.

class HitCount(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    hits = models.IntegerField(default=0)

    def __str__(self):
        return f'number of hits {self.hits}'

class MonitoredItem(models.Model):
    text = models.CharField(max_length=100)
    hitcount = GenericRelation(HitCount, null=True, blank=True)

    @transaction.atomic
    def save(self, *args, **kwargs):
        super(MonitoredItem, self).save(*args, **kwargs)
        if self.hitcount.count()==0:
            self.hitcount.add(HitCount.objects.create(content_object=self))

    def __str__(self):
        return self.text

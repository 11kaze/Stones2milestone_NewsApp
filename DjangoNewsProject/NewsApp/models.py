from django.db import models
from datetime import datetime
# Create your models here.

class NewsModal(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=70)
    Description = models.TextField()
    Created_date = models.DateTimeField( default=datetime.now())
    Author = models.CharField(max_length=20)
    Image = models.ImageField(null=True,blank=True,upload_to='newsImages')
    Source = models.URLField()

    def __str__(self):
        return self.name
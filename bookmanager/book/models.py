from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class BookInfo(models.Model):
    # Book name
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class PeopleInfo(models.Model):
    # People name
    name = models.CharField(max_length=10)
    # Gender
    gender = models.BooleanField()
    # Foreign key to book table
    book = models.ForeignKey(BookInfo, on_delete=CASCADE)
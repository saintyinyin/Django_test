from django.db import models

# Create your models here.
class BookInfo(models.Model):
    name = models.CharField(max_length=10, unique=True)
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table='bookinfo'
        verbose_name='书籍管理'

class PeopleInfo(models.Model):
    GENDER_CHOICE = (
        (1,'MALE'),
        (2,'FEMALE')
    )
    name = models.CharField(max_length=10,unique=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=1)
    description = models.TextField(max_length=100, null=True)
    is_delete = models.BooleanField(default=False)

    # foreign key
    # will add _id suffix to foreign key name
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table='peopleinfo'
        verbose_name='人物管理'
                
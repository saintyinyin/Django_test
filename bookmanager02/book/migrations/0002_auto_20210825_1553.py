# Generated by Django 3.2.6 on 2021-08-25 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='peopleinfo',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='book.bookinfo'),
        ),
        migrations.AddField(
            model_name='peopleinfo',
            name='description',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='peopleinfo',
            name='gender',
            field=models.SmallIntegerField(choices=[(1, 'MALE'), (2, 'FEMALE')], default=1),
        ),
        migrations.AddField(
            model_name='peopleinfo',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='peopleinfo',
            name='name',
            field=models.CharField(default='BookInfo', max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='peopleinfo',
            table='peopleinfo',
        ),
    ]

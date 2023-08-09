# Generated by Django 3.2.12 on 2023-07-23 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='surname',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.TextField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.TextField(null=True, unique=True),
        ),
    ]

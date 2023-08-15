# Generated by Django 3.2.12 on 2023-08-11 19:23

from django.db import migrations, models
import django_ckeditor_5.fields
import phonenumber_field.modelfields
import shop.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DevelopmentTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(blank=True, max_length=20, null=True)),
                ('patronymic', models.CharField(blank=True, max_length=20, null=True)),
                ('telephone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True)),
                ('mail', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('role', models.TextField(blank=True, max_length=200, null=True)),
                ('description_work', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images_development_team')),
            ],
            options={
                'verbose_name': 'команда разработчиков',
                'verbose_name_plural': 'Команда разработчиков',
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=500, null=True)),
                ('answer', django_ckeditor_5.fields.CKEditor5Field(max_length=2500, null=True)),
            ],
            options={
                'verbose_name': 'полезная/справочная информация',
                'verbose_name_plural': 'Полезная/справочная информация',
            },
        ),
        migrations.CreateModel(
            name='FeaturesSoftware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=5000, null=True)),
                ('operating_system', models.CharField(blank=True, max_length=50, null=True)),
                ('video_card', models.TextField(blank=True, max_length=1000, null=True)),
                ('hard_disk_mb', models.PositiveIntegerField(blank=True, null=True)),
                ('min_ram_mb', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'параметры програмного обеспечения',
                'verbose_name_plural': 'Параметры програмного обеспечения',
            },
        ),
        migrations.CreateModel(
            name='ImageCollectionForIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images_for_index')),
            ],
            options={
                'verbose_name': 'картинки на главной страницы',
                'verbose_name_plural': 'Картинки на главной страницы',
            },
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=14)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images_software')),
            ],
            options={
                'verbose_name': 'программное обеспечение',
                'verbose_name_plural': 'Програмное обеспечение',
            },
        ),
        migrations.CreateModel(
            name='SoftwareCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images_software_category')),
            ],
            options={
                'verbose_name': 'категории программного обеспечения',
                'verbose_name_plural': 'Категории программного обеспечения',
            },
        ),
        migrations.CreateModel(
            name='UsersQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userquestion', models.TextField(max_length=500)),
                ('question_timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('upload', models.FileField(blank=True, null=True, upload_to=shop.models.user_directory_path)),
            ],
            options={
                'verbose_name': 'вопросы от пользователей',
                'verbose_name_plural': 'Вопросы от пользователей',
            },
        ),
    ]

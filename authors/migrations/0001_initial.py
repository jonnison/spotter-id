# Generated by Django 5.1.1 on 2024-09-18 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('gender', models.CharField(blank=True, max_length=55, null=True, verbose_name='Gender')),
                ('image_url', models.CharField(blank=True, max_length=55, null=True, verbose_name='Image URL')),
                ('about', models.TextField(blank=True, null=True, verbose_name='About')),
                ('reviews_count', models.IntegerField(default=0, verbose_name='Reviews Count')),
                ('fans_count', models.IntegerField(default=0, verbose_name='Fans Count')),
                ('ratings_count', models.IntegerField(default=0, verbose_name='Rating Count')),
                ('average_rating', models.DecimalField(decimal_places=2, default=0, max_digits=3, verbose_name='Average Rating')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

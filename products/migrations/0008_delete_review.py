# Generated by Django 4.0.4 on 2022-05-26 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_review_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]

# Generated by Django 5.1.7 on 2025-03-07 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='protfolio',
            name='url',
            field=models.TextField(null=True),
        ),
    ]

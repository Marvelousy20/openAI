# Generated by Django 5.0.2 on 2024-04-11 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('replicate', '0002_predictionmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='predictionmodel',
            name='model',
            field=models.CharField(default='', max_length=300),
        ),
    ]
# Generated by Django 5.0.3 on 2024-04-03 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_statisticspage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statisticspage',
            name='works_completed',
            field=models.IntegerField(default='', verbose_name='Loyihalar soni'),
        ),
    ]

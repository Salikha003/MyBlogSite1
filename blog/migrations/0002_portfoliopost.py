# Generated by Django 5.0.3 on 2024-03-31 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='portfolio/', verbose_name='Post rasmi')),
                ('about', models.TextField(verbose_name="Post haqida qisqacha ma'lumot")),
                ('name', models.CharField(max_length=50, verbose_name='Post nomi')),
                ('data', models.DateField(verbose_name="Post qo'yilgan sanasi")),
            ],
            options={
                'verbose_name': 'Portfolio posti',
                'verbose_name_plural': 'Portfolio posti',
                'db_table': 'PortfolioPost',
                'managed': True,
            },
        ),
    ]

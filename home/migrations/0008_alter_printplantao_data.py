# Generated by Django 5.0.7 on 2024-09-20 02:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_printplantao_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printplantao',
            name='data',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

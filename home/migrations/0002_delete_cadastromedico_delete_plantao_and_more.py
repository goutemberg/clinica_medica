# Generated by Django 5.0.7 on 2024-07-16 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='cadastroMedico',
        ),
        migrations.DeleteModel(
            name='plantao',
        ),
        migrations.DeleteModel(
            name='valorPlantao',
        ),
    ]

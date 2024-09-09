# Generated by Django 5.0.7 on 2024-09-06 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_plantao_medico_responsavel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrintPlantao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=14)),
                ('especialidade', models.CharField(max_length=100)),
                ('valor_plantao', models.DecimalField(decimal_places=2, max_digits=10)),
                ('horas', models.DecimalField(decimal_places=2, max_digits=5)),
                ('valor_horas', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_imposto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_a_receber', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
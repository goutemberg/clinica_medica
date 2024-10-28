import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroEmpresa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('razao_social', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=18, unique=True, validators=[django.core.validators.RegexValidator(message='CNPJ deve estar no formato 00.000.000/0000-00', regex='^\\d{2}\\.\\d{3}\\.\\d{3}/\\d{4}-\\d{2}$')])),
                ('inscricao_estadual', models.CharField(blank=True, max_length=255, null=True)),
                ('cep', models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(message='CEP deve estar no formato XXXXX-XXX', regex='^\\d{5}-?\\d{3}$')])),
                ('logradouro', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=5)),
                ('bairro', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=2)),
                ('telefone', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message='Telefone deve estar no formato (XX) XXXX-XXXX ou (XX) XXXXX-XXXX', regex='^\\(?\\d{2}\\)?[\\s-]?\\d{4,5}-?\\d{4}$')])),
                ('email', models.EmailField(max_length=50, validators=[django.core.validators.EmailValidator(message='Email inválido')])),
                ('isento_tributacao', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='BancoEmpresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banco', models.CharField(max_length=50)),
                ('agencia', models.CharField(max_length=10)),
                ('conta', models.CharField(max_length=10)),
                ('titular_conta', models.CharField(max_length=255)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bancos', to='home.cadastroempresa')),
            ],
        ),
        migrations.CreateModel(
            name='CadastroMedico',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='CPF deve estar no formato 000.000.000-00', regex='^\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}$')])),
                ('especialidade', models.CharField(max_length=100)),
                ('crm', models.CharField(max_length=20)),
                ('celular', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message='Celular deve estar no formato (XX) XXXXX-XXXX', regex='^\\(?\\d{2}\\)?[\\s-]?\\d{4,5}-?\\d{4}$')])),
                ('logradouro', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=5)),
                ('complemento', models.CharField(blank=True, max_length=255, null=True)),
                ('bairro', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=2)),
                ('telefone1', models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(message='Telefone deve estar no formato (XX) XXXX-XXXX ou (XX) XXXXX-XXXX', regex='^\\(?\\d{2}\\)?[\\s-]?\\d{4,5}-?\\d{4}$')])),
                ('telefone2', models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(message='Telefone deve estar no formato (XX) XXXX-XXXX ou (XX) XXXXX-XXXX', regex='^\\(?\\d{2}\\)?[\\s-]?\\d{4,5}-?\\d{4}$')])),
                ('email', models.EmailField(max_length=100, validators=[django.core.validators.EmailValidator(message='Email inválido')])),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicos', to='home.cadastroempresa')),
            ],
        ),
        migrations.CreateModel(
            name='BancoMedico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banco', models.CharField(max_length=50)),
                ('agencia', models.CharField(max_length=10)),
                ('conta', models.CharField(max_length=10)),
                ('titular_conta', models.CharField(max_length=255)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bancos', to='home.cadastromedico')),
            ],
        ),
        migrations.CreateModel(
            name='ContatoEmpresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pessoa_contato', models.CharField(max_length=50)),
                ('email_contato', models.EmailField(max_length=50, validators=[django.core.validators.EmailValidator(message='Email inválido')])),
                ('telefone_contato', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message='Telefone deve estar no formato (XX) XXXX-XXXX ou (XX) XXXXX-XXXX', regex='^\\(?\\d{2}\\)?[\\s-]?\\d{4,5}-?\\d{4}$')])),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contatos', to='home.cadastroempresa')),
            ],
        ),
        migrations.CreateModel(
            name='ImpostoEmpresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxa_administrativa', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('valor_imposto', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='impostos', to='home.cadastroempresa')),
            ],
        ),
        migrations.CreateModel(
            name='Plantao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data_inicio', models.DateField(default=django.utils.timezone.now)),
                ('hora_inicio', models.TimeField(default=django.utils.timezone.now)),
                ('data_termino', models.DateField(default=django.utils.timezone.now)),
                ('hora_termino', models.TimeField(default=django.utils.timezone.now)),
                ('especialidade', models.CharField(max_length=255)),
                ('tipo_plantao', models.CharField(max_length=20)),
                ('quantidade_horas', models.DecimalField(decimal_places=2, max_digits=5)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(max_length=12)),
                ('contato_emergencia', models.CharField(max_length=255)),
                ('equipamentos_necessarios', models.TextField(blank=True, null=True)),
                ('cargos_auxiliares', models.TextField(blank=True, null=True)),
                ('substituto', models.CharField(blank=True, max_length=255, null=True)),
                ('observacoes', models.TextField(blank=True, max_length=255, null=True)),
                ('medico_responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plantoes', to='home.cadastromedico')),
            ],
        ),
        migrations.CreateModel(
            name='ValorPlantao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_12h', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('valor_por_hora', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('valor_semana', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('valor_fim_semana', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='valores_plantao', to='home.cadastroempresa')),
            ],
        ),
    ]
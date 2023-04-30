# Generated by Django 4.2 on 2023-04-30 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dieta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diaSemana', models.CharField(blank=True, choices=[('Segunda-feira', 'SF'), ('Terça-feira', 'TF'), ('Quarta-feira', 'QAF'), ('Quinta-feira', 'QIF'), ('Sexta-feira', 'SF'), ('Sábado', 'S'), ('Domingo', 'D')], max_length=50, null=True)),
                ('quantidade', models.CharField(max_length=255)),
                ('alimento', models.CharField(max_length=255)),
                ('horario', models.CharField(max_length=255)),
            ],
        ),
    ]

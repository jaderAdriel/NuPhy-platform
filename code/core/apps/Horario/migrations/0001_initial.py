# Generated by Django 4.2 on 2023-04-30 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horarioComeco', models.DateTimeField()),
                ('horarioFim', models.DateTimeField()),
            ],
        ),
    ]

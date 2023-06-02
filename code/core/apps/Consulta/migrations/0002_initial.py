# Generated by Django 4.2 on 2023-04-30 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('Consulta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulta',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_paciente', to='accounts.usuario'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='profissional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_professional', to='accounts.usuario'),
        ),
    ]
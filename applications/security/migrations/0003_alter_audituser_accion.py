# Generated by Django 5.2.1 on 2025-06-16 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0002_audituser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audituser',
            name='accion',
            field=models.CharField(choices=[('ADICION', 'ADICION'), ('MODIFICACION', 'MODIFICACION'), ('ELIMINACION', 'ELIMINACION')], max_length=15, verbose_name='Accion'),
        ),
    ]

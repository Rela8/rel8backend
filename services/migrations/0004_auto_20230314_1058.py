# Generated by Django 3.2.13 on 2023-03-14 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20230314_0809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reissuanceofcertform',
            name='year_turn_over',
        ),
        migrations.AddField(
            model_name='yearlyturnover',
            name='reissuance_of_cert_form',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.reissuanceofcertform'),
        ),
    ]

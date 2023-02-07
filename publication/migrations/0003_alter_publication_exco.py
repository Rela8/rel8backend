# Generated by Django 3.2.13 on 2023-02-07 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_membershipgrade'),
        ('publication', '0002_publicationcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='exco',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.excorole'),
        ),
    ]
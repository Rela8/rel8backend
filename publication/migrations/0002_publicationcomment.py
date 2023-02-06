# Generated by Django 3.2.13 on 2023-02-05 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20230205_0220'),
        ('publication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicationComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.memeber')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publication.publication')),
            ],
        ),
    ]

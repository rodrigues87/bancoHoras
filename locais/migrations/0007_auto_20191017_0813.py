# Generated by Django 2.2.6 on 2019-10-17 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locais', '0006_auto_20191017_0811'),
    ]

    operations = [
        migrations.AddField(
            model_name='localqdi',
            name='idLocalQdi',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='localqo',
            name='idLocalQo',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

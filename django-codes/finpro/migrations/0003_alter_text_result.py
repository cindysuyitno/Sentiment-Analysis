# Generated by Django 3.2.15 on 2022-09-12 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finpro', '0002_auto_20220912_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='result',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
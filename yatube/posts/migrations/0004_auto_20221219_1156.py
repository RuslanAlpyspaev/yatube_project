# Generated by Django 2.2.19 on 2022-12-19 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20221219_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.TextField(),
        ),
    ]
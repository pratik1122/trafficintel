# Generated by Django 2.2.7 on 2019-12-04 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=None),
        ),
    ]

# Generated by Django 4.2 on 2024-05-05 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='gst_no',
            field=models.CharField(default='N/A', max_length=20),
        ),
    ]

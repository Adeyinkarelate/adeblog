# Generated by Django 4.0.3 on 2022-03-21 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-date_created',)},
        ),
    ]
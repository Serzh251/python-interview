# Generated by Django 3.2.9 on 2021-11-29 16:19

import django.contrib.sites.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_goods_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='category',
            managers=[
                ('objects', django.contrib.sites.managers.CurrentSiteManager('site')),
            ],
        ),
    ]

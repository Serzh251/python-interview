# Generated by Django 3.2.9 on 2021-11-29 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('mainapp', '0003_alter_goods_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site'),
        ),
        migrations.AddField(
            model_name='goods',
            name='site',
            field=models.ManyToManyField(to='sites.Site'),
        ),
    ]

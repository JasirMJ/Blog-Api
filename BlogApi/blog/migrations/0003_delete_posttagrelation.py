# Generated by Django 2.1.7 on 2019-07-02 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_posttagrelation'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PostTagRelation',
        ),
    ]

# Generated by Django 2.1.7 on 2019-07-02 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_posttagrelation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posttagrelation',
            name='id_post',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='posttagrelation',
            name='id_tag',
            field=models.CharField(max_length=200),
        ),
    ]

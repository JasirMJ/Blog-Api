# Generated by Django 2.1.7 on 2019-07-01 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=100, null=True)),
                ('post_name', models.CharField(max_length=100, null=True)),
                ('post_description', models.CharField(max_length=200, null=True)),
                ('post_tag_id', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tag_name', models.CharField(max_length=200)),
            ],
        ),
    ]

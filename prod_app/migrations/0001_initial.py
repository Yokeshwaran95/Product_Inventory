# Generated by Django 4.0.2 on 2022-02-24 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ElasticDemo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=200)),
                ('productprice', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 4.1 on 2022-09-02 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CricketTeamSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=256)),
                ('lastName', models.CharField(max_length=256)),
                ('cricketTeam', models.CharField(max_length=256)),
                ('role', models.CharField(max_length=256)),
            ],
        ),
        migrations.AlterField(
            model_name='cartitems',
            name='product_quantity',
            field=models.PositiveIntegerField(),
        ),
    ]

# Generated by Django 4.2 on 2023-05-21 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://th.bing.com/th/id/OIP.CAXQe3AgWFel1hIzxDZ6owEsDg?w=268&h=201&c=7&r=0&o=5&pid=1.7', max_length=500),
        ),
    ]
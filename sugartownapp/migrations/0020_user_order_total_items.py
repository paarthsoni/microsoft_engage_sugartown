# Generated by Django 3.2.5 on 2022-05-25 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sugartownapp', '0019_alter_user_order_orderplaced_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_order',
            name='total_items',
            field=models.IntegerField(default=0),
        ),
    ]

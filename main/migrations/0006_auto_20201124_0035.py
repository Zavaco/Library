# Generated by Django 3.1.3 on 2020-11-23 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20201123_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='book_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.book'),
        ),
        migrations.DeleteModel(
            name='BookInfo',
        ),
    ]

# Generated by Django 3.2.4 on 2021-07-01 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(default=21, on_delete=django.db.models.deletion.PROTECT, to='app.categoria'),
            preserve_default=False,
        ),
    ]

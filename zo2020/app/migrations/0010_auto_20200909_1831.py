# Generated by Django 3.0.7 on 2020-09-09 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20200907_1455'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hub',
            old_name='hub_type',
            new_name='type',
        ),
        migrations.AlterField(
            model_name='hub',
            name='main_contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hubs_main_contact', to='app.Account', verbose_name='Main Contact'),
        ),
    ]
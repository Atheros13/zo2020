# Generated by Django 3.0.7 on 2020-09-05 03:30

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_user_temporary_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=254)),
                ('admins', models.ManyToManyField(related_name='hubs_admin', to='app.Account')),
            ],
        ),
        migrations.CreateModel(
            name='HubType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='HubAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line1', models.CharField(blank=True, max_length=30)),
                ('line2', models.CharField(blank=True, max_length=30)),
                ('suburb', models.CharField(blank=True, max_length=30)),
                ('town_city', models.CharField(blank=True, max_length=30)),
                ('postcode', models.CharField(blank=True, max_length=13)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('hub', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='app.Hub')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='hub',
            name='hub_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hubs', to='app.HubType'),
        ),
        migrations.AddField(
            model_name='hub',
            name='main_contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hubs_main_contact', to='app.Account'),
        ),
    ]

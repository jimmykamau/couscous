# Generated by Django 2.2.7 on 2019-11-14 15:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import localflavor.generic.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Debtor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('iban', localflavor.generic.models.IBANField(include_countries=None, max_length=34, use_nordea_extensions=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debtor_creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 4.2 on 2023-06-11 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advertising', '0002_rename_client_id_advertising_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertising',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
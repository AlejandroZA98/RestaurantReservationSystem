# Generated by Django 5.0.3 on 2025-01-08 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation_app', '0002_rename_tables_table_table_alter_table_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='disponibility',
            field=models.BooleanField(default=None),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.1.2 on 2020-10-22 12:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0003_delete_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='writing',
            name='author',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='accounts.myuser'),
            preserve_default=False,
        ),
    ]

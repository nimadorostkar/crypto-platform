# Generated by Django 4.1.2 on 2022-10-29 07:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('api_key', models.CharField(max_length=256)),
                ('api_secret', models.CharField(max_length=256)),
                ('api_passphrase', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('status', models.CharField(choices=[('not-active', 'not-active'), ('active', 'active')], default='not-active', max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-23 19:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
                ('incident_category', models.IntegerField(choices=[(1, 'Fly Tipping'), (2, 'Noise Pollution'), (3, 'Abandoned Vehicle'), (4, 'Littering'), (5, 'Statutory Nuisance (e.g. odour, light, etc.)'), (6, 'Presentation of Waste (Domestic)'), (7, 'Presentation of Waste (Commercial)'), (8, 'Atmospheric Pollution (e.g. smoke, fumes, etc.)'), (9, 'Accumulation of Waste'), (10, 'Trade Waste Checking'), (11, 'ASB (Anti-Social Behaviour)')])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('received_on', models.DateTimeField()),
                ('details', models.TextField()),
                ('closed_on', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incidents', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]

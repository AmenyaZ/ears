# Generated by Django 2.0 on 2019-06-20 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veoc', '0018_event_action_taken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='incident_status',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='veoc.incident_status'),
        ),
        migrations.AlterField(
            model_name='event',
            name='incident_status',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='veoc.incident_status'),
        ),
    ]

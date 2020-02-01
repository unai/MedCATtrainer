# Generated by Django 2.2.9 on 2020-01-31 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20200131_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='icdcode',
            name='cdb',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ConceptDB'),
        ),
        migrations.AddField(
            model_name='opcscode',
            name='cdb',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ConceptDB'),
        ),
    ]

# Generated by Django 2.1.5 on 2019-01-30 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accountsapp', '0004_auto_20190130_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteeruser',
            name='enrolled_Organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='volunteers', to='accountsapp.OrganizationUser', to_field='organization_Name'),
        ),
    ]

# Generated by Django 4.2 on 2024-10-28 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gym', '0006_alter_member_address_alter_member_email_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default='M', max_length=1),
        ),
    ]
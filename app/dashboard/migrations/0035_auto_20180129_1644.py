# Generated by Django 2.0 on 2018-01-29 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0034_auto_20180129_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bounty',
            old_name='claimeee_address',
            new_name='fulfiller_address',
        ),
        migrations.RenameField(
            model_name='bounty',
            old_name='claimee_email',
            new_name='fulfiller_email',
        ),
        migrations.RenameField(
            model_name='bounty',
            old_name='claimee_github_username',
            new_name='fulfiller_github_username',
        ),
        migrations.RenameField(
            model_name='bounty',
            old_name='claimee_metadata',
            new_name='fulfiller_metadata',
        ),
        migrations.RenameField(
            model_name='bounty',
            old_name='claimee_name',
            new_name='fulfiller_name',
        ),
        migrations.AlterField(
            model_name='bounty',
            name='accepted',
            field=models.BooleanField(default=False, help_text='Whether the bounty has been done'),
        ),
    ]

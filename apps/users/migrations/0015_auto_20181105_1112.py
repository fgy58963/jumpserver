# Generated by Django 2.1.1 on 2018-11-05 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20180816_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginlog',
            name='reason',
            field=models.SmallIntegerField(choices=[(0, '-'), (1, 'Username/password check failed'), (2, 'MFA authentication failed'), (3, 'Username does not exist')], default=0, verbose_name='Reason'),
        ),
        migrations.AlterField(
            model_name='loginlog',
            name='username',
            field=models.CharField(max_length=128, verbose_name='Username'),
        ),
    ]

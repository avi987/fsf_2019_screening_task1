# Generated by Django 2.1a1 on 2019-03-20 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_status',
            field=models.CharField(choices=[('Planned', 'Planned'), ('in_progress', 'in_progress'), ('done', 'done'), ('terminated', 'terminated')], default='Planned', max_length=30),
        ),
    ]

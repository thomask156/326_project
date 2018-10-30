# Generated by Django 2.0.1 on 2018-10-26 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('argue_app', '0003_auto_20181025_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lobby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_participants', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='argument',
            name='opponent',
        ),
        migrations.RemoveField(
            model_name='argument',
            name='outcome',
        ),
        migrations.RemoveField(
            model_name='argument',
            name='profile',
        ),
        migrations.AddField(
            model_name='argument',
            name='description',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='argument',
            name='status',
            field=models.CharField(default='Ongoing', max_length=200),
        ),
        migrations.AddField(
            model_name='argument',
            name='topic_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='argue_app.Topic'),
        ),
        migrations.AddField(
            model_name='lobby',
            name='arguement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='argue_app.Argument'),
        ),
        migrations.AddField(
            model_name='lobby',
            name='participants',
            field=models.ManyToManyField(to='argue_app.Profile'),
        ),
    ]
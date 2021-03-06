# Generated by Django 2.0.1 on 2018-11-02 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('argue_app', '0006_auto_20181030_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatLobby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lobby_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='lobby',
            name='argument',
        ),
        migrations.RemoveField(
            model_name='lobby',
            name='participants',
        ),
        migrations.RemoveField(
            model_name='chatmessage',
            name='profile',
        ),
        migrations.AddField(
            model_name='argument',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator', to='argue_app.Profile'),
        ),
        migrations.AddField(
            model_name='argument',
            name='max_participants',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='argument',
            name='participants',
            field=models.ManyToManyField(to='argue_app.Profile'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='writer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='argue_app.Profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='argument',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='argue_app.Topic'),
        ),
        migrations.DeleteModel(
            name='Lobby',
        ),
        migrations.AddField(
            model_name='argument',
            name='chat_lobby',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='argue_app.ChatLobby'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='chat_lobby',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='argue_app.ChatLobby'),
            preserve_default=False,
        ),
    ]

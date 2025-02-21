# Generated by Django 4.2 on 2025-02-21 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dislikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('dislikes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disliked_by', to='user_profile.userprofile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disliked_profiles', to='user_profile.userprofile')),
            ],
            options={
                'ordering': ['-created_at'],
                'unique_together': {('user', 'dislikes')},
            },
        ),
    ]

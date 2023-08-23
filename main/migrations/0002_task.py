# Generated by Django 4.1 on 2022-12-18 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24, verbose_name='name')),
                ('description', models.CharField(max_length=150, verbose_name='description')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('is_completed', models.BooleanField(verbose_name='Complete')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
            ],
        ),
    ]

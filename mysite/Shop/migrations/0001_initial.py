# Generated by Django 4.0.4 on 2022-05-26 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=250)),
                ('pc_name', models.CharField(max_length=250)),
                ('model', models.CharField(max_length=250)),
                ('pc_logo', models.CharField(max_length=1000)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='HardDrive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drive_name', models.CharField(max_length=250)),
                ('pc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.pc')),
            ],
        ),
        migrations.CreateModel(
            name='GraphicsCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(max_length=250)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.pc')),
            ],
        ),
    ]
# Generated by Django 3.1.7 on 2021-03-24 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('total_debt', models.FloatField()),
                ('punctuation', models.CharField(choices=[('B', 'Bueno'), ('M', 'Malo'), ('R', 'Regular')], default='R', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('state', models.CharField(choices=[('NR', 'No revisado'), ('A', 'Aprobado'), ('NA', 'No aprobado')], default='NR', max_length=2)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.client')),
            ],
        ),
    ]
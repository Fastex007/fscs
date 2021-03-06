# Generated by Django 2.2.9 on 2020-12-16 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import lib.UpperCharField


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AircraftType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('edited_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Изменено')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название типа ВС')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='aircrafttype_creator', to=settings.AUTH_USER_MODEL, verbose_name='Создал')),
                ('edited_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='aircrafttype_editor', to=settings.AUTH_USER_MODEL, verbose_name='Изменил')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('edited_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Изменено')),
                ('registration_number', lib.UpperCharField.UpperCharField(max_length=10, unique=True, verbose_name='Регистрационный номер')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='aircraft_creator', to=settings.AUTH_USER_MODEL, verbose_name='Создал')),
                ('edited_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='aircraft_editor', to=settings.AUTH_USER_MODEL, verbose_name='Изменил')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='types', to='references.AircraftType')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

# Generated by Django 3.0.8 on 2020-07-13 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Interests', models.TextField(blank=True, null=True)),
                ('hobbies', models.CharField(blank=True, max_length=200, null=True)),
                ('jungs_type', models.CharField(blank=True, max_length=20, null=True)),
                ('history', models.TextField(blank=True, null=True)),
                ('first_meeting', models.TextField(blank=True, null=True)),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('employer', models.CharField(blank=True, max_length=200, null=True)),
                ('relationship', models.CharField(blank=True, max_length=200, null=True)),
                ('misc_1', models.CharField(blank=True, max_length=200, null=True)),
                ('misc_2', models.CharField(blank=True, max_length=200, null=True)),
                ('misc_3', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]

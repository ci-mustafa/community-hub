# Generated by Django 5.0.6 on 2024-05-27 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communityhub', '0003_family'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]

# Generated by Django 5.1.7 on 2025-03-09 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EducationalOpportunity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_info', models.CharField(blank=True, max_length=255, null=True)),
                ('external_link', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='educational_opportunities/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

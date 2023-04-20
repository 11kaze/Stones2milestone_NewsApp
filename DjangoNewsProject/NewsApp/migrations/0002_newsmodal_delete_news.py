# Generated by Django 4.2 on 2023-04-19 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsModal',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=70)),
                ('Description', models.TextField()),
                ('Created_date', models.DateTimeField(auto_now_add=True)),
                ('Author', models.CharField(max_length=20)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='newImages')),
                ('Source', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]
# Generated by Django 4.1.7 on 2023-03-02 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('course_Id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('duration', models.IntegerField()),
                ('fees', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('rollnum', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('email_token', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('is_email_varified', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]

# Generated by Django 3.2.16 on 2023-01-29 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(choices=[('MR', 'Mr.'), ('MRS', 'Mrs.'), ('MS', 'Ms.')], max_length=3)),
                ('birth_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('authors', models.ManyToManyField(to='myforms.Author')),
            ],
        ),
    ]
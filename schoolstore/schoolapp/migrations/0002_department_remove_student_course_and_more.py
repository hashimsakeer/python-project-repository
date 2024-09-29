# Generated by Django 4.2.8 on 2024-02-05 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.RemoveField(
            model_name='student',
            name='department',
        ),
        migrations.AlterField(
            model_name='student',
            name='materials_provide',
            field=models.ManyToManyField(blank=True, to='schoolapp.material'),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolapp.department')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(blank=True, to='schoolapp.course'),
        ),
        migrations.AddField(
            model_name='student',
            name='department',
            field=models.ManyToManyField(blank=True, to='schoolapp.department'),
        ),
    ]
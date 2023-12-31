# Generated by Django 4.2.5 on 2023-10-05 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course_catg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Coursess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('discount_price', models.IntegerField()),
                ('about_course', models.TextField()),
                ('course_categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms_app.course_catg')),
            ],
            options={
                'verbose_name_plural': 'Courses',
            },
        ),
    ]

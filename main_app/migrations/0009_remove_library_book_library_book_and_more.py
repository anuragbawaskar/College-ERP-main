# Generated by Django 4.0.6 on 2022-08-31 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_student_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='library',
            name='book',
        ),
        migrations.AddField(
            model_name='library',
            name='book',
            field=models.ManyToManyField(to='main_app.book'),
        ),
        migrations.RemoveField(
            model_name='library',
            name='student',
        ),
        migrations.AddField(
            model_name='library',
            name='student',
            field=models.ManyToManyField(to='main_app.student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.book'),
        ),
    ]

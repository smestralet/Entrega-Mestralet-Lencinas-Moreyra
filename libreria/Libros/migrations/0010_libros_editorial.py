# Generated by Django 4.0.4 on 2022-06-07 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Libros', '0009_remove_libros_editorial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libros',
            name='editorial',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='Libros.editorial'),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.0.4 on 2022-07-04 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Libros', '0012_libros_editorial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='editorial',
            options={'verbose_name': 'editorial', 'verbose_name_plural': 'editoriales'},
        ),
        migrations.AlterModelOptions(
            name='libros',
            options={'verbose_name': 'libro', 'verbose_name_plural': 'libros'},
        ),
        migrations.AlterModelOptions(
            name='locales',
            options={'verbose_name': 'local', 'verbose_name_plural': 'locales'},
        ),
    ]

# Generated by Django 4.0.4 on 2022-06-07 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Libros', '0005_alter_libros_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='editorial',
            name='foto',
            field=models.ImageField(default='x', upload_to=''),
            preserve_default=False,
        ),
    ]
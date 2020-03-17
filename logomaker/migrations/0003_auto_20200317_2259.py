# Generated by Django 3.0.4 on 2020-03-17 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logomaker', '0002_category_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='logo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logoname', models.CharField(max_length=100)),
                ('logoimage', models.ImageField(default='mypic', upload_to='upload/')),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
    ]

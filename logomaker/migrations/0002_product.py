# Generated by Django 3.0.4 on 2020-03-17 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logomaker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('logoname', models.CharField(max_length=200)),
                ('price', models.FloatField(default=0.0, max_length=1000)),
                ('companyname', models.CharField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logomaker.category')),
            ],
        ),
    ]

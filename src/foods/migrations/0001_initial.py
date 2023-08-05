# Generated by Django 4.2.3 on 2023-08-05 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_add_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=30, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(default='/images/categories/default.jpeg', upload_to='images/categories/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_add_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(default='/images/foods/default.jpg', upload_to='images/foods/')),
                ('available_quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('discount', models.FloatField(default=0.0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='foods.category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

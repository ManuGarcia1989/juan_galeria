# Generated by Django 2.2.8 on 2021-09-03 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Obras', '0007_obras_checkpoint'),
    ]

    operations = [
        migrations.CreateModel(
            name='Light',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(help_text='#FFF', max_length=150)),
                ('type', models.CharField(help_text='One of ambient, directional, hemisphere, point, spot.', max_length=150)),
                ('intensity', models.FloatField(verbose_name='Intensity')),
                ('position', models.CharField(help_text='0 0 0', max_length=150)),
                ('rotation', models.CharField(help_text='0 0 0', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.FileField(upload_to='objects3D/')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='imagenesGafas/')),
                ('dimentions', models.CharField(max_length=150)),
                ('date', models.DateField(verbose_name='Date Pices')),
                ('price', models.CharField(max_length=150)),
                ('checkpoint', models.CharField(help_text='Donde va a teletransportarse el observador ex:0 0 0', max_length=150)),
                ('position', models.CharField(help_text='0 0 0', max_length=150)),
                ('rotation', models.CharField(help_text='0 0 0', max_length=150)),
                ('scale', models.CharField(help_text='0 0 0', max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='Lights',
        ),
        migrations.DeleteModel(
            name='Obras',
        ),
        migrations.AlterField(
            model_name='scene',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Scene Name'),
        ),
    ]
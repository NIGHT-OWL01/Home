# Generated by Django 4.0.2 on 2022-05-10 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='speciality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='doctor.speciality'),
        ),
    ]
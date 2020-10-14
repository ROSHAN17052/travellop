# Generated by Django 3.1.1 on 2020-09-20 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0006_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newstrip',
            fields=[
                ('besttrip_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='enroll.besttrip')),
                ('title1', models.CharField(max_length=40)),
            ],
            bases=('enroll.besttrip',),
        ),
    ]

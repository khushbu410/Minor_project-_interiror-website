# Generated by Django 5.0.3 on 2024-10-08 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_direction_room_alter_booking_designer_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VastuUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_plan', models.ImageField(upload_to='house_plans/')),
                ('direction', models.CharField(choices=[('N', 'North'), ('S', 'South'), ('E', 'East'), ('W', 'West')], max_length=20)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='vasturule',
            name='direction',
        ),
        migrations.RemoveField(
            model_name='vasturule',
            name='room',
        ),
        migrations.DeleteModel(
            name='UserVastuCheck',
        ),
        migrations.DeleteModel(
            name='VastuRule',
        ),
    ]

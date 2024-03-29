# Generated by Django 4.1.1 on 2022-11-14 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('manufacturer', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('image', models.ImageField(default='component_images/default_component.png', upload_to='component_images')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('component_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='components.component')),
                ('color', models.CharField(max_length=50)),
            ],
            bases=('components.component',),
        ),
        migrations.CreateModel(
            name='Cooler',
            fields=[
                ('component_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='components.component')),
                ('type', models.CharField(max_length=50)),
            ],
            bases=('components.component',),
        ),
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('component_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='components.component')),
                ('speed', models.FloatField()),
            ],
            bases=('components.component',),
        ),
        migrations.CreateModel(
            name='Graphics',
            fields=[
                ('component_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='components.component')),
                ('size', models.FloatField()),
            ],
            bases=('components.component',),
        ),
        migrations.CreateModel(
            name='Motherboard',
            fields=[
                ('component_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='components.component')),
                ('socket', models.CharField(max_length=50)),
            ],
            bases=('components.component',),
        ),
        migrations.CreateModel(
            name='PowerSupply',
            fields=[
                ('component_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='components.component')),
                ('power', models.IntegerField()),
            ],
            bases=('components.component',),
        ),
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('component_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='components.component')),
                ('speed', models.FloatField()),
                ('size', models.FloatField()),
            ],
            bases=('components.component',),
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('component_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='components.component')),
                ('size', models.FloatField()),
            ],
            bases=('components.component',),
        ),
    ]

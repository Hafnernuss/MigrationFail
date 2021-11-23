# Generated by Django 3.2.9 on 2021-11-23 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('some_other_base_field', models.IntegerField(default=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SomeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('some_field', models.IntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='DerivedModel',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sample.basemodel')),
                ('relation', models.ManyToManyField(related_name='_sample_derivedmodel_relation_+', to='sample.SomeModel')),
            ],
            bases=('sample.basemodel',),
        ),
    ]
# Generated by Django 2.0.4 on 2018-04-29 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('porcion', models.IntegerField()),
                ('kcal', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Calculadora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kcal_ideal', models.FloatField()),
                ('alimentos', models.ManyToManyField(to='calculadora.Alimento')),
            ],
        ),
        migrations.CreateModel(
            name='GrupoAlimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('kcal_prom', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='alimento',
            name='grupo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculadora.GrupoAlimento'),
        ),
    ]

# Generated by Django 4.0 on 2021-12-22 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debtor_name', models.CharField(max_length=50, verbose_name='Name debtor')),
                ('debtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='NotMyMoney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suma', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Suma')),
                ('comment_text', models.CharField(max_length=200, verbose_name='Text comment')),
                ('calculation', models.BooleanField()),
                ('pub_date', models.DateTimeField(verbose_name='Date publication')),
                ('money_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finances.people')),
            ],
        ),
        migrations.CreateModel(
            name='MyMoney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suma', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Suma')),
                ('comment_text', models.CharField(max_length=200, verbose_name='Text comment')),
                ('calculation', models.BooleanField()),
                ('pub_date', models.DateTimeField(verbose_name='Date publication')),
                ('money_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finances.people')),
            ],
        ),
    ]

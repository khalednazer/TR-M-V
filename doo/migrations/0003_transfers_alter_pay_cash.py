# Generated by Django 5.1.2 on 2024-11-27 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doo', '0002_remove_pay_credit_pay_cash_pay_credit_no_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frome', models.CharField(max_length=9)),
                ('to', models.CharField(max_length=9)),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('done', 'done'), ('Erorr', 'Erorr')], max_length=10)),
                ('amount', models.CharField(max_length=6)),
            ],
        ),
        migrations.AlterField(
            model_name='pay',
            name='cash',
            field=models.IntegerField(auto_created=True, default=0, null=True),
        ),
    ]

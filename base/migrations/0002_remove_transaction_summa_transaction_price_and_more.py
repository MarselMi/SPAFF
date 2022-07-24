# Generated by Django 4.0.6 on 2022-07-24 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='summa',
        ),
        migrations.AddField(
            model_name='transaction',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Цена заказа'),
        ),
        migrations.AlterField(
            model_name='client',
            name='email_adress',
            field=models.EmailField(max_length=254, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='client',
            name='middle_name',
            field=models.CharField(default=None, max_length=20, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='client',
            name='telephone_number',
            field=models.CharField(max_length=12, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='client',
            name='user_status',
            field=models.CharField(choices=[('delete', 'delete'), ('active', 'active')], default='active', max_length=10, verbose_name='Статус клиента'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='client_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='base.client', verbose_name='Идентификационный номер клиента'),
        ),
    ]
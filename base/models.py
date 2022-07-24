from django.db import models


class Client(models.Model):
    '''Таблица данных о клиенте, с возможностью выбора желаемого
    статуса'''

    STATUS = (('delete', 'delete'),
              ('active', 'active'),
              )

    STATUS_DEFAULT = 'active'

    MIDLE_NAME_DEFAULT = None

    name = models.CharField(max_length=20, verbose_name='Имя')
    surname = models.CharField(max_length=20, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=20, default=MIDLE_NAME_DEFAULT, null=True, verbose_name='Отчество')
    email_adress = models.EmailField(verbose_name='Электронная почта')
    telephone_number = models.CharField(max_length=12, verbose_name='Телефон')
    password = models.TextField(verbose_name='Пароль')
    user_status = models.CharField(default=STATUS_DEFAULT, max_length=10, choices=STATUS, verbose_name='Статус клиента')

    def __str__(self):
        return f'id={self.id}, Имя = {self.name}, Фамилия = {self.surname}'


class Transaction(models.Model):
    '''Таблица транзакций, для работы с админки'''

    DIRECTION = (('In', 'In'),
                 ('Out', 'Out'),
                 )

    STATUS = (('confirm', 'confirm'),
              ('noconfirm', 'noconfirm'),
              )

    price = models.DecimalField(null=True, decimal_places=2, max_digits=10, verbose_name='Цена заказа')
    direct_transaction = models.CharField(max_length=5, choices=DIRECTION, verbose_name='Направление транзакции')
    status_transaction = models.CharField(max_length=12, choices=STATUS, verbose_name='Статус транзакции')
    client_id = models.ForeignKey(Client, null=True, on_delete=models.CASCADE, related_name='children', verbose_name='Идентификационный номер клиента')

    def __str__(self):
        return f'{self.client_id}'


class Change(models.Model):
    name = models.CharField(default=None, null=True, max_length=20, verbose_name='Имя')
    surname = models.CharField(default=None, null=True, max_length=20, verbose_name='Фамилия')
    middle_name = models.CharField(default=None, null=True, max_length=20, verbose_name='Отчество')
    email_adress = models.EmailField(default=None, null=True, verbose_name='Изменение электронной почты')
    telephone_number = models.CharField(default=None, null=True, max_length=12, verbose_name='Изменение телефона')
    password = models.TextField(default=None, null=True, verbose_name='Изменение пароля')
    user_status = models.CharField(default=None, null=True, max_length=10, verbose_name='Изменение статуса клиента')
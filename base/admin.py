from django.contrib import admin
from .models import Transaction, Client, Change


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'middle_name', 'email_adress', 'telephone_number', 'user_status')
    list_display_links = ('name', )
    list_editable = ('user_status', )


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'direct_transaction', 'status_transaction', 'price', )
    list_display_links = ('client_id', )
    list_editable = ('status_transaction', 'price', 'direct_transaction', )


class ChangeAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'middle_name', 'email_adress', 'telephone_number', 'user_status')
    list_display_links = ('name',)


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Change, ChangeAdmin)
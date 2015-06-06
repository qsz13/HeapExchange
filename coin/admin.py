from django.contrib import admin

# Register your models here.
from coin.models import Balance, Transfer


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    pass

@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    pass
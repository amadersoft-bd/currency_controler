from django.contrib import admin
from .models import Balance,TransferBalance,BalanceWithdraw,BalanceExchange
# Register your models here.
admin.site.register(Balance)
admin.site.register(TransferBalance)
admin.site.register(BalanceWithdraw)
admin.site.register(BalanceExchange)
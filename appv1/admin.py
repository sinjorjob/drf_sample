from django.contrib import admin
from .models import Bank, Branch


class BankAdmin(admin.ModelAdmin):
   list_display=('pk','name', 'bank_code')
 
class BranchAdmin(admin.ModelAdmin):
   list_display=('pk','bank_name', 'branch_name', 'branch_code')

admin.site.register(Bank, BankAdmin)
admin.site.register(Branch, BranchAdmin)


from rest_framework import serializers	
from .models import Bank, Branch


class BankSerializer(serializers.ModelSerializer):	
    class Meta:
        model = Bank
        fields = ('name', 'bank_code')	



class BranchSerializer(serializers.ModelSerializer):
    bank_name = BankSerializer()  #追加	
    class Meta:
        model = Branch
        fields = ('bank_name', 'branch_name', 'branch_code')	

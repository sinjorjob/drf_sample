import django_filters			
from rest_framework import viewsets, filters
from .models import Bank, Branch
from .serializer import BankSerializer, BranchSerializer


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    filter_fields = ('bank_name',)  #add

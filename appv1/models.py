from django.db import models


class Bank(models.Model):
    class Meta:
        verbose_name ="銀行名"
        verbose_name_plural = "銀行名"

    name = models.CharField("銀行名",max_length=255)
    bank_code = models.CharField("銀行コード",max_length=8)
    def __str__(self):
        return self.name


class Branch(models.Model):
    class Meta:
        verbose_name ="支店名"
        verbose_name_plural = "支店名"

    bank_name = models.ForeignKey(Bank, on_delete=models.CASCADE)	
    branch_name = models.CharField("支店名",max_length=255)
    branch_code = models.CharField("支店コード",max_length=6)
    def __str__(self):
        return self.branch_name


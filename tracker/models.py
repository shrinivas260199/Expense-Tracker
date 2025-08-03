from django.db import models

# Create your models here.

class CurrentBalance(models.Model):
    current_balance = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return f"{self.current_balance}"

class TrackingHistory(models.Model):
    Current_balance = models.ForeignKey(CurrentBalance, on_delete=models.CASCADE)
    expense_type = models.CharField(choices=(('CREDIT', 'CREDIT'), ('DEBIT', 'DEBIT')), max_length=50, editable=False)
    amount = models.FloatField(editable=False)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"Amount is {self.amount} for {self.description} and it's expense type is {self.expense_type}"
from django.shortcuts import render, redirect
from .models import TrackingHistory, CurrentBalance
from django.db.models import Sum

def index(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        amount = float(request.POST.get('amount'))

        # Determine the type of transaction
        expense_type = 'CREDIT' if amount >= 0 else 'DEBIT'

        # Get or create the CurrentBalance instance (only one with id=1)
        current_balance_obj, _ = CurrentBalance.objects.get_or_create(id=1)

        # Create a new TrackingHistory record
        TrackingHistory.objects.create(
            amount=amount,
            expense_type=expense_type,
            Current_balance=current_balance_obj,
            description=description
        )

        # Update the current balance value
        current_balance_obj.current_balance += amount
        current_balance_obj.save()

        return redirect('/')
    
    income=0 
    expense = 0
    for tracking_history in TrackingHistory.objects.all():
        if tracking_history.expense_type == 'CREDIT':
            income += tracking_history.amount
        else:
            expense += tracking_history.amount

    current_balance_obj, _ = CurrentBalance.objects.get_or_create(id=1)
    context = {'income':income, 'expense':expense,'transactions':TrackingHistory.objects.all(), 'current_balance':current_balance_obj}

    return render(request, 'tracker/index.html',context)

def delete_transaction(request, id):
    tracking_history = TrackingHistory.objects.filter(id = id)

    if tracking_history.exists():
        current_balance_obj, _ = CurrentBalance.objects.get_or_create(id=1)
        tracking_history = tracking_history[0]
        current_balance_obj.current_balance -= tracking_history.amount
        current_balance_obj.save()


    tracking_history.delete()
    return redirect('/')
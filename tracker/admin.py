from django.contrib import admin
from .models import *

admin.site.site_header = 'Expense Tracker'
admin.site.site_title = 'Expense Tracker'
#admin.site.site_url = 'Expense Tracker'

class TrackingHistoryAdmin(admin.ModelAdmin):
    list_display = ["description",
        "expense_type",
        "amount",
        "created_at",
        "Current_balance",
        "expense"
    ]

    def expense(self, obj):
        if obj.amount > 0:
            return 'Positive'
        else:
            return 'Negative'
        
    @admin.action(description="Mark selected entries as amount received")
    def make_amount_received(modeladmin, request, queryset):
        queryset.update(expense_type="Amount Received")
    
    actions = ["make_amount_received"]

    search_fields = ["amount", "description"]
    list_filter = ["expense_type"]

    ordering = ["created_at"]

# Register your models here.
admin.site.register(CurrentBalance)
admin.site.register(TrackingHistory,TrackingHistoryAdmin)
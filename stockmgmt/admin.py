from django.contrib import admin
from .models import Stock, Category, StockHistory

from .forms import StockCreationForm


class StockCreateAdmin(admin.ModelAdmin):
    list_display = ['category', 'item_name', 'quantity']
    form = StockCreationForm
    list_filter = ['category']
    search_fields = ['category', 'item_name']


# Register your models here.
admin.site.register(Stock, StockCreateAdmin)
admin.site.register(Category)
admin.site.register(StockHistory)

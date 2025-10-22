from django.contrib import admin
from .models import Claim

@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('id',)
    readonly_fields = ('created_at',)
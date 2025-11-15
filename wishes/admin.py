
from django.contrib import admin
from .models import Wish

@admin.register(Wish)
class WishAdmin(admin.ModelAdmin):
    list_display = ('name','short_message','created_at')
    readonly_fields = ('created_at',)

    def short_message(self, obj):
        return obj.message[:60]
    short_message.short_description = 'Message preview'

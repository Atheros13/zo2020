from django.contrib import admin
from app.models import Hub

def activate_selected_hubs(modeladmin, request, queryset):

    for hub in queryset:
        hub.is_active = True
        hub.save()
        hub.send_activation_email()
activate_selected_hubs.short_description = 'Make selected Hubs active'

class HubAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'description', 'email', 'main_contact']
    actions = [activate_selected_hubs]

    def type(self, obj):
        return obj.type.id


admin.site.register(Hub, HubAdmin)

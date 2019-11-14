from django.contrib import admin

from .models import Debtor


class DebtorAdmin(admin.ModelAdmin):
    exclude = ['created_by']
    list_display = (
        'email',
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(created_by=request.user)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if not obj:
            return True
        if obj.created_by == request.user:
            return True
        return False

    has_delete_permission = has_change_permission


admin.site.register(Debtor, DebtorAdmin)

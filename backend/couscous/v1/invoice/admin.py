from django.contrib import admin

import couscous.v1.debtor.models as debtor_models

from .models import Invoice


class InvoiceAdmin(admin.ModelAdmin):
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(debtor__created_by=request.user)

    def has_change_permission(self, request, obj=None):
        if not obj:
            return True
        if obj.debtor.created_by == request.user:
            return True
        return False

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "debtor":
            kwargs["queryset"] = debtor_models.Debtor.objects.filter(
                created_by=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


    has_delete_permission = has_change_permission

admin.site.register(Invoice, InvoiceAdmin)

from django.db.models import Count
from django_filters import rest_framework as filters

import couscous.v1.debtor.models as debtor_models


class DebtorFilter(filters.FilterSet):
    status = filters.CharFilter(field_name='debtor_invoice__status')
    invoice_count = filters.NumberFilter(method='filter_invoice_count')

    def filter_invoice_count(self, queryset, name, value):
        if value:
            queryset = queryset.annotate(
                number_of_invoices=Count('debtor_invoice')
            ).filter(number_of_invoices=value)
        return queryset
    
    class Meta:
        model = debtor_models.Debtor
        fields = ['status', 'invoice_count']

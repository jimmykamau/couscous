from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions

import couscous.v1.invoice.models as invoice_models
import couscous.v1.invoice.serializers as invoice_serializers


class ListInvoiceView(generics.ListAPIView):
    """
    List Invoices
    """
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = invoice_serializers.InvoiceSerializer
    queryset = invoice_models.Invoice.objects.all()
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filter_fields = ('debtor__email', 'status', 'amount', 'due_date')
    ordering_fields = ['debtor__email', 'status', 'amount', 'due_date']

    def get_queryset(self):
        return self.queryset.filter(debtor__created_by=self.request.user)

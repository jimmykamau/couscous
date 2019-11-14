from rest_framework import generics, permissions

import couscous.v1.invoice.models as invoice_models
import couscous.v1.invoice.serializers as invoice_serializers


class ListInvoiceView(generics.ListAPIView):
    """
    List Invoices
    """
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = invoice_serializers.InvoiceSerializer
    queryset = invoice_models.Invoice.objects.all()

    def get_queryset(self):
        return self.queryset.filter(debtor__created_by=self.request.user)

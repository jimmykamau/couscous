from rest_framework import serializers

import couscous.v1.invoice.models as invoice_models


class InvoiceSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='debtor.email')

    class Meta:
        model = invoice_models.Invoice
        fields = ('email', 'status', 'amount', 'due_date')

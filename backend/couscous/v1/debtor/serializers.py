from rest_framework import serializers

import couscous.v1.debtor.models as debtor_models


class DebtorSerializer(serializers.ModelSerializer):
    open_invoices = serializers.IntegerField()
    paid_invoices = serializers.IntegerField()
    overdue_invoices = serializers.IntegerField()

    class Meta:
        model = debtor_models.Debtor
        fields = (
            'email', 'iban', 'open_invoices', 'paid_invoices',
            'overdue_invoices'
        )

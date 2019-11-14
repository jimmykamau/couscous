from rest_framework import serializers

import couscous.v1.debtor.models as debtor_models


class DebtorSerializer(serializers.ModelSerializer):

    class Meta:
        model = debtor_models.Debtor
        fields = (
            'email', 'iban', 'open_invoices', 'paid_invoices',
            'overdue_invoices'
        )

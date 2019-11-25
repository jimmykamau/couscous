from django.db.models import Count, Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions

import couscous.v1.debtor.filtersets as debtor_filtersets
import couscous.v1.debtor.models as debtor_models
import couscous.v1.debtor.serializers as debtor_serializers


class ListDebtorView(generics.ListAPIView):
    """
    List debtors
    """
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = debtor_serializers.DebtorSerializer
    queryset = debtor_models.Debtor.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = debtor_filtersets.DebtorFilter

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user).annotate(
            open_invoices=Count(
                'debtor_invoice', filter=Q(
                    debtor_invoice__status='OP'
                )
            ),
            paid_invoices=Count(
                'debtor_invoice', filter=Q(
                    debtor_invoice__status='PA'
                )
            ),
            overdue_invoices=Count(
                'debtor_invoice', filter=Q(
                    debtor_invoice__status='OV'
                )
            )
        )

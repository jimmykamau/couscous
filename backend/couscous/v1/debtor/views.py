from rest_framework import generics, permissions
import couscous.v1.debtor.models as debtor_models
import couscous.v1.debtor.serializers as debtor_serializers


class ListDebtorView(generics.ListAPIView):
    """
    List debtors
    """
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = debtor_serializers.DebtorSerializer
    queryset = debtor_models.Debtor.objects.all()

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)

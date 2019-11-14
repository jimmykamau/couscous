from django.db import models
from django.utils.translation import gettext_lazy as _

import couscous.v1.debtor.models as debtor_models


class Invoice(models.Model):
    INVOICE_STATUS_CHOICES = (
        ('OP', 'Open'),
        ('PA', 'Paid'),
        ('OV', 'Overdue'),
        ('CA', 'Canceled')
    )
    debtor = models.ForeignKey(
        debtor_models.Debtor, on_delete=models.CASCADE,
        related_name='debtor_invoice'
    )
    status = models.CharField(_('status'), max_length=2, choices=INVOICE_STATUS_CHOICES)
    amount = models.DecimalField(_('amount'), max_digits=10, decimal_places=2)
    due_date = models.DateField(_('due date'))

    def __str__(self):
        return f"#{self.pk} - {self.debtor.email}"

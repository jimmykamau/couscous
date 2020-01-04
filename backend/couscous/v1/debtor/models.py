from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count, Q
from django.utils.translation import gettext_lazy as _
from localflavor.generic.models import IBANField


class DebtorInvoiceManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(
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


class Debtor(models.Model):
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='debtor_creator'
    )
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    email = models.EmailField(_('email address'), unique=True)
    iban = IBANField()

    invoice_count_objects = DebtorInvoiceManager()
    objects = models.Manager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.iban}"

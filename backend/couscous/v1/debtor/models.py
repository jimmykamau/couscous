from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from localflavor.generic.models import IBANField


class Debtor(models.Model):
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='debtor_creator'
    )
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    email = models.EmailField(_('email address'), unique=True)
    iban = IBANField()

    @property
    def open_invoices(self):
        return len(self.debtor_invoice.filter(status='OP'))
    
    @property
    def paid_invoices(self):
        return len(self.debtor_invoice.filter(status='PA'))
    
    @property
    def overdue_invoices(self):
        return len(self.debtor_invoice.filter(status='OV'))

    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.iban}"

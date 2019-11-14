import random

from django.urls import reverse
from rest_framework.test import APITestCase

import couscous.v1.invoice.tests.factories as invoice_factories
import couscous.v1.tests.factories as couscous_factories
from couscous.v1.debtor import logger

from .factories import DebtorFactory


class ListDebtorViewTests(APITestCase):

    def setUp(self):
        self.admin_user = couscous_factories.UserFactory()
        self.client.force_authenticate(user=self.admin_user)
        self.debtors = DebtorFactory.create_batch(3, created_by=self.admin_user)
        self.invoices = invoice_factories.InvoiceFactory.create_batch(
            3, debtor=self.debtors[1]
        )
        self.url = reverse('v1:list-debtors')
    
    def tearDown(self):
        self.client.force_authenticate(user=None)
    
    def test_cannot_list_without_staff_rights(self):
        self.admin_user.is_staff = False
        self.admin_user.save()
        response = self.client.get(
            self.url, format='json'
        )
        self.assertEqual(403, response.status_code)
    
    def test_list_debtors(self):
        response = self.client.get(
            self.url, format='json'
        )
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            len(self.debtors),
            len(response.data)
        )
        self.assertCountEqual(
            [
                'email', 'iban', 'open_invoices',
                'paid_invoices', 'overdue_invoices'
            ],
            response.data[0]
        )
    
    def test_cannot_view_other_user_debtors(self):
        other_admin = couscous_factories.UserFactory()
        self.client.force_authenticate(user=other_admin)
        response = self.client.get(
            self.url, format='json'
        )
        self.assertEqual(200, response.status_code)
        self.assertFalse(response.data)
    
    def test_filter_results(self):
        #  Filter by invoice status
        status = random.choice(
            [
                ("OP", "open_invoices"),
                ("PA", "paid_invoices"),
                ("OV", "overdue_invoices")
            ]
        )
        url = f"{self.url}?status={status[0]}"
        response = self.client.get(url, format='json')
        self.assertEqual(200, response.status_code)
        for debtor in response.data:
            self.assertLess(
                0,
                debtor[status[1]]
            )

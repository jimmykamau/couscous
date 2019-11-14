from django.urls import reverse
from rest_framework.test import APITestCase

import couscous.v1.debtor.tests.factories as debtor_factories
import couscous.v1.tests.factories as couscous_factories
from couscous.v1.invoice import logger

from .factories import InvoiceFactory


class ListInvoiceViewTests(APITestCase):

    def setUp(self):
        self.admin_user = couscous_factories.UserFactory()
        self.client.force_authenticate(user=self.admin_user)
        self.debtors = debtor_factories.DebtorFactory.create_batch(
            3, created_by=self.admin_user
        )
        self.invoices = InvoiceFactory.create_batch(
            5, debtor=self.debtors[0]
        )
        self.url = reverse('v1:list-invoices')

    def tearDown(self):
        self.client.force_authenticate(user=None)
    
    def test_list_invoices(self):
        response = self.client.get(
            self.url, format='json'
        )
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            len(self.invoices),
            len(response.data)
        )
        
        # Check the content of the returned data
        self.assertCountEqual(
            ['email', 'status', 'amount', 'due_date'],
            response.data[0]
        )
    
    def test_cannot_list_invoices_without_auth(self):
        # Test for user that didn't create invoices
        other_user = couscous_factories.UserFactory()
        self.client.force_authenticate(user=other_user)
        response = self.client.get(
            self.url, format='json'
        )
        self.assertEqual(200, response.status_code)
        self.assertFalse(response.data)
        
        # Test for user without staff rights
        self.admin_user.is_staff = False
        self.admin_user.save()
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get(
            self.url, format='json'
        )
        self.assertEqual(403, response.status_code)
        
        # Test for logged out user
        self.client.force_authenticate(user=None)
        response = self.client.get(
            self.url, format='json'
        )
        self.assertEqual(403, response.status_code)
    
    def test_filter_results(self):
        other_debtor_invoices = InvoiceFactory.create_batch(2, debtor=self.debtors[1])
        
        # Filter by debtor email
        url = f"{self.url}?debtor__email={self.debtors[1].email}"
        response = self.client.get(
            url, format='json'
        )
        self.assertEqual(
            200, response.status_code
        )
        self.assertEqual(
            len(other_debtor_invoices),
            len(response.data)
        )

        # Filter by status
        status = other_debtor_invoices[0].status
        url = f"{self.url}?status={status}"
        response = self.client.get(
            url, format='json'
        )
        self.assertEqual(200, response.status_code)
        for invoice in response.data:
            self.assertEqual(status, invoice['status'])
        
        # Filter by amount
        amount = float(other_debtor_invoices[1].amount)
        url = f"{self.url}?amount={amount}"
        response = self.client.get(
            url, format='json'
        )
        self.assertEqual(200, response.status_code)
        for invoice in response.data:
            self.assertEqual(amount, float(invoice['amount']))
        
        # Filter by due date
        due_date = self.invoices[2].due_date.strftime('%Y-%m-%d')
        url = f"{self.url}?due_date={due_date}"
        response = self.client.get(
            url, format='json'
        )
        self.assertEqual(200, response.status_code)
        for invoice in response.data:
            self.assertEqual(due_date, invoice['due_date'])

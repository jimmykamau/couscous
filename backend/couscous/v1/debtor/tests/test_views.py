from django.urls import reverse
from rest_framework.test import APITestCase

import couscous.v1.tests.factories as couscous_factories
from couscous.v1.debtor import logger

from .factories import DebtorFactory


class ListDebtorViewTests(APITestCase):

    def setUp(self):
        self.admin_user = couscous_factories.UserFactory()
        self.client.force_authenticate(user=self.admin_user)
        self.debtors = DebtorFactory.create_batch(3, created_by=self.admin_user)
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
    
    def test_cannot_view_other_user_debtors(self):
        other_admin = couscous_factories.UserFactory()
        self.client.force_authenticate(user=other_admin)
        response = self.client.get(
            self.url, format='json'
        )
        self.assertEqual(200, response.status_code)
        self.assertFalse(response.data)

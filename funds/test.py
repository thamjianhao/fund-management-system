from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.db import IntegrityError
from .models import Fund

from django.db import connection


class FundAPITestCase(TestCase):
    def setUp(self):
        # Initialize test client and create sample fund data for tests
        self.client = APIClient()
        self.fund_data = {
            "fund_id": "FUND001",
            "fund_name": "Test Fund",
            "fund_manager_name": "John Doe",
            "fund_description": "A test fund for unit testing.",
            "fund_nav": "100.00",
            "date_of_creation": "2023-01-01",
            "fund_performance": "10.00"
        }

    def test_create_fund_success(self):
        # Test successful fund creation via API
        response = self.client.post(
            '/funds/', data=self.fund_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Fund.objects.count(), 1)
        fund = Fund.objects.get(fund_id="FUND001")
        self.assertEqual(fund.fund_name, "Test Fund")

    def test_get_fund_not_found(self):
        # Test 404 response for non-existent fund
        response = self.client.get('/funds/FUND999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {"error": "Fund not found"})

    def test_create_fund_invalid_nav(self):
        # Test validation for negative NAV value
        invalid_data = self.fund_data.copy()
        invalid_data["fund_id"] = "FUND002"
        invalid_data["fund_nav"] = "-10.00"
        response = self.client.post(
            '/funds/', data=invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("fund_nav", response.data)

    def test_create_fund_invalid_performance(self):
        # Test validation for performance exceeding maximum value
        invalid_data = self.fund_data.copy()
        invalid_data["fund_id"] = "FUND003"
        invalid_data["fund_performance"] = "1500.00"  # Exceeds the max of 1000
        response = self.client.post(
            '/funds/', data=invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("fund_performance", response.data)

    def test_update_fund_success(self):
        # Test successful fund update operation
        self.client.post('/funds/', data=self.fund_data, format='json')
        updated_data = self.fund_data.copy()
        updated_data["fund_name"] = "Updated Fund"
        response = self.client.put(
            '/funds/FUND001/', data=updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        fund = Fund.objects.get(fund_id="FUND001")
        self.assertEqual(fund.fund_name, "Updated Fund")

    def test_delete_fund_success(self):
        # Test successful fund deletion
        self.client.post('/funds/', data=self.fund_data, format='json')
        response = self.client.delete('/funds/FUND001/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Fund.objects.count(), 0)

    def test_sql_query_fund_creation(self):
        # Test direct SQL query to verify fund creation in database
        self.client.post('/funds/', data=self.fund_data, format='json')
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM funds_fund WHERE fund_id = %s", ["FUND001"])
            row = cursor.fetchone()
        self.assertEqual(row[0], 1)

    def test_duplicate_fund_id(self):
        # Test database integrity for duplicate fund_id
        self.client.post('/funds/', data=self.fund_data, format='json')
        with self.assertRaises(IntegrityError):
            Fund.objects.create(**self.fund_data)

    def test_fund_performance_edge_values(self):
        # Test boundary values for fund performance (min and max)
        edge_case_data = self.fund_data.copy()
        edge_case_data["fund_id"] = "FUND003"
        edge_case_data["fund_performance"] = "1000.00"  # Max valid value
        response = self.client.post('/funds/', data=edge_case_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        edge_case_data = self.fund_data.copy()
        edge_case_data["fund_id"] = "FUND004"
        edge_case_data["fund_performance"] = "-100.00"  # Min valid value
        response = self.client.post('/funds/', data=edge_case_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

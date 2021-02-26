from django.test import TestCase
from .models import Countries
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


class ViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.countries_data = {'name': 'sudan'}
        self.response = self.client.post(
            reverse('create'),
            self.countries_data,
            format="json")

    def test_api_can_create_a_countries(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_country(self):
        countries = Countries.objects.get()
        response = self.client.get(
            reverse('details', kwargs={'pk': countries.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, countries)

    def test_api_can_update_countries(self):
        countries = Countries.objects.get()
        change_country = {'name': 'sudan'}
        response = self.client.put(
            reverse('details', kwargs={'pk': countries.id}),
            change_country, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_countries(self):
        countries = Countries.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': Countries.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)


class ModelTestCase(TestCase):

    def setUp(self):
        self.country_name = "sudan"
        self.countries = Countries(name=self.country_name)

    def test_model_can_create_a_countries(self):
        count = Countries.objects.count()
        self.countries.save()
        new_count = Countries.objects.count()
        self.assertNotEqual(count, new_count)

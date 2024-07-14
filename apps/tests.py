from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from apps.models import Program

class ProgramTests(APITestCase):

    def setUp(self):
        # This method will run before any test case
        self.program1 = Program.objects.create(name='Program 1', duration_months=6)
        self.program2 = Program.objects.create(name='Program 2', duration_months=12)

    def test_list_programs(self):
        url = reverse('program-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_program(self):
        url = reverse('program-list')
        data = {'name': 'Program 3', 'duration_months': 9}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Program.objects.count(), 3)
        self.assertEqual(Program.objects.get(id=response.data['id']).name, 'Program 3')

    def test_retrieve_program(self):
        url = reverse('program-detail', kwargs={'pk': self.program1.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.program1.name)

    def test_update_program(self):
        url = reverse('program-detail', kwargs={'pk': self.program1.pk})
        data = {'name': 'Updated Program', 'duration_months': 10}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.program1.refresh_from_db()
        self.assertEqual(self.program1.name, 'Updated Program')
        self.assertEqual(self.program1.duration_months, 10)

    def test_delete_program(self):
        url = reverse('program-detail', kwargs={'pk': self.program1.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Program.objects.count(), 1)

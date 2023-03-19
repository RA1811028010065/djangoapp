from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from api.models import Task

class TaskTestCase(TestCase):
    def setUp(self):
        self.api_client = APIClient()

    def create_task(self, title='Test task', description='', completed=False):
        return Task.objects.create(title=title, description=description, completed=completed)

    def authenticate_client(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        self.api_client.force_authenticate(user=user)
class TaskListTests(TaskTestCase):
    def test_task_list(self):
        task1 = self.create_task()
        task2 = self.create_task()

        url = reverse('task-list')
        response = self.api_client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)
        self.assertEqual(response.json()[0]['title'], task1.title)
        self.assertEqual(response.json()[1]['title'], task2.title)

class TaskDetailTests(TaskTestCase):
    def test_task_detail(self):
        task = self.create_task()

        url = reverse('task-detail', kwargs={'pk': task.id})
        response = self.api_client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['title'], task.title)

class CreateTaskTests(TaskTestCase):
    def test_create_task(self):
        self.authenticate_client()

        url = reverse('task-list')
        data = {'title': 'New task'}
        response = self.api_client.post(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().title, 'New task')

class UpdateTaskTests(TaskTestCase):
    def test_update_task(self):
        self.authenticate_client()

        task = self.create_task()

        url = reverse('task-detail', kwargs={'pk': task.id})
        data = {'title': 'Updated task'}
        response = self.api_client.put(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().title, 'Updated task')

class DeleteTaskTests(TaskTestCase):
    def test_delete_task(self):
        self.authenticate_client()

        task = self.create_task()

        url = reverse('task-detail', kwargs={'pk': task.id})
        response = self.api_client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

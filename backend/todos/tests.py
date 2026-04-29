from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Todo


class TodoModelTest(TestCase):
    # Declare attributes so mypy knows they exist on the class
    todo: Todo

    @classmethod
    def setUpTestData(cls) -> None:
        cls.todo = Todo.objects.create(
            title = "First Todo",
            body = "This is the task",
        )

    def test_model_content(self) -> None:
        self.assertEqual(self.todo.title, "First Todo")
        self.assertEqual(self.todo.body, "This is the task")
        self.assertEqual(str(self.todo), "First Todo")

    
class TodoAPITests(APITestCase):
    # Attributes declared so mypy knows they are in class
    todo: Todo

    @classmethod
    def setUpTestData(cls) -> None:
        cls.todo = Todo.objects.create(
            title = "Test Todo",
            body = "Test body text",
        )
        cls.list_url = reverse("todo_list")
        cls.detail_url = reverse("todo_detail", args=[cls.todo.id])

    def test_list_todo(self) -> None:
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertGreaterEqual(len(response.data), 1)

    def test_detail_todo(self) -> None:
        response = self.client.get(self.detail_url)
        self.assertEqual(response.data["title"], self.todo.title)
        self.assertEqual(response.data["body"], self.todo.body)

    def test_todo_not_found(self) -> None:
        response = self.client.get(reverse("todo_detail", args=[999]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
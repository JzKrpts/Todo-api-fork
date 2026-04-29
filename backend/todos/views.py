from rest_framework import generics

from .models import Todo
from .serializers import TodoSerializer


class ListTodo(generics.ListAPIView[Todo]):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveAPIView[Todo]):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

from rest_framework import serializers

from .models import Todo

# [Todo] is type argument to help mypy infer types
class TodoSerializer(serializers.ModelSerializer[Todo]):
    class Meta:
        model = Todo
        fields = (
            "id",
            "title",
            "body",
        )
from rest_framework import serializers

from todo.models import ToDo


class ToDoSerializers(serializers.ModelSerializer):
    """
    
    """

    class Meta:
        model = ToDo
        fileds = ["title", "content", "active", "status"]
        exclude = []

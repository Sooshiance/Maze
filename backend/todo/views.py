from rest_framework import generics, permissions

from todo.models import ToDo
from todo.serializers import ToDoSerializers


class AllTaskAPIView(generics.ListAPIView):
    """"""
    serializer_class = [ToDoSerializers]
    queryset = ToDo.objects.all()
    permission_classes = [permissions.AllowAny]


class SingleTaskAPIView(generics.RetrieveAPIView):
    """"""
    serializer_class = [ToDoSerializers]
    permission_classes = [permissions.AllowAny]
    queryset = ToDo.objects.all()

    def get_object(self):
        pk = self.kwargs['pk']
        t = ToDo.objects.get(pk=pk)
        return t


class CreateTaskAPIView(generics.ListCreateAPIView):
    """"""
    serializer_class = [ToDoSerializers]
    queryset = ToDo.objects.all()
    permission_classes = [permissions.AllowAny]


class DeleteTaskAPIView(generics.RetrieveDestroyAPIView):
    """"""
    serializer_class = [ToDoSerializers]
    queryset = ToDo.objects.all()
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        pk = self.kwargs['pk']
        t = ToDo.objects.get(pk=pk)
        return t

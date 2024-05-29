from rest_framework import generics, permissions, response, status

from todo.models import ToDo
from todo.serializers import ToDoSerializers


class AllTaskAPIView(generics.GenericAPIView):
    """"""
    serializer_class = [ToDoSerializers]
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        q = ToDo.objects.all()
        s = ToDoSerializers(instance=q, many=True)
        return response.Response(data=s.data, status=status.HTTP_200_OK)


class SingleTaskAPIView(generics.GenericAPIView):
    """"""
    serializer_class = [ToDoSerializers]
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        t = ToDo.objects.get(pk=pk)
        s = ToDoSerializers(instance=t)
        return response.Response(data=s.data, status=status.HTTP_200_OK)


class CreateTaskAPIView(generics.GenericAPIView):
    """"""
    serializer_class = [ToDoSerializers]
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        s = ToDoSerializers(data=request.data)
        if s.is_valid():
            s.save()
            return response.Response(data=s.data, status=status.HTTP_201_CREATED)
        else:
            return response.Response(data=s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class DeleteTaskAPIView(generics.RetrieveDestroyAPIView):
    """"""
    serializer_class = [ToDoSerializers]
    queryset = ToDo.objects.all()
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        pk = self.kwargs['pk']
        t = ToDo.objects.get(pk=pk)
        return t


class UpdateTaskAPIView(generics.GenericAPIView):
    """"""
    serializer_class = [ToDoSerializers]
    permission_classes = [permissions.AllowAny]

    def post(self, request, pk):
        t = ToDo.objects.get(pk=pk)
        s = ToDoSerializers(instance=t, data=request.data)
        if s.is_valid():
            s.save()
            return response.Response(data=s.data, status=status.HTTP_205_RESET_CONTENT)
        else:
            return response.Response(data=s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

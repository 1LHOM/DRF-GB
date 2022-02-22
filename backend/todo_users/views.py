from rest_framework.viewsets import ModelViewSet
from .models import ToDoUser
from .serializers import AuthorModelSerializer


class ToDoUserViewSet(ModelViewSet):
    queryset = ToDoUser.objects.all()
    serializer_class = AuthorModelSerializer


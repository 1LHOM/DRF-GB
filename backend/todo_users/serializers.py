from rest_framework.serializers import HyperlinkedModelSerializer
from .models import ToDoUser


class AuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ToDoUser
        fields = ('username', 'first_name', 'last_name', 'email')

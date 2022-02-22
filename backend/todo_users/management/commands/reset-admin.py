from django.core.management import BaseCommand
from todo_users.models import ToDoUser


class Command(BaseCommand):
    """
    This command will create 1 superuser and 3 default users,
        default superuser
                username: admin
                password: geekbrains
    """

    def handle(self, *args, **options):
        ToDoUser.objects.all().delete()
        ToDoUser.objects.create_superuser('admin', 'admin@example.com', 'geekbrains',)
        ToDoUser.objects.create_user('user0', 'user0@mail.com', 'QWERasdf')
        ToDoUser.objects.create_user('test1', 'user1@mail.com', 'QWERASDF')
        ToDoUser.objects.create_user('user2', 'user2@mail.com', 'QWERasdf1234')


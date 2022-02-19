from django.core.management import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    """
    This command will create 1 superuser and 3 default users,
        default superuser
                username: admin
                password: adminPASS1
    """

    def handle(self, *args, **options):
        User.objects.all().delete()
        User.objects.create_superuser('admin', 'admin@example.com', 'adminPASS1',)
        User.objects.create_user('user0', 'user0@mail.com', 'QWERasdf')
        User.objects.create_user('test1', 'user1@mail.com', 'QWERASDF')
        User.objects.create_user('user2', 'user2@mail.com', 'QWERasdf1234')


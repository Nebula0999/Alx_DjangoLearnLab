from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from relationship_app.models import Book

class Command(BaseCommand):
    help = 'Create groups and assign permissions'

    def handle(self, *args, **kwargs):
        # Define group names
        group_permissions = {
            'Editors': ['can_create', 'can_edit'],
            'Viewers': ['can_view'],
            'Admins': ['can_create', 'can_edit', 'can_delete', 'can_view'],
        }

        # Create groups and assign permissions
        for group_name, permissions in group_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for perm in permissions:
                permission = Permission.objects.get(codename=perm, content_type__model='book')
                group.permissions.add(permission)
            self.stdout.write(self.style.SUCCESS(f'Group "{group_name}" created/updated with permissions'))
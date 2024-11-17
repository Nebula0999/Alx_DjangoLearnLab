# Permissions and Groups Setup in Django

## Custom Permissions
The `Book` model has custom permissions defined:
- `can_view`: Allows viewing books.
- `can_create`: Allows creating new book entries.
- `can_edit`: Allows editing existing book entries.
- `can_delete`: Allows deleting book entries.

## Groups and Permissions
The following groups are set up with assigned permissions:
- **Editors**: Can create and edit books.
- **Viewers**: Can only view books.
- **Admins**: Have full permissions (view, create, edit, delete).

## Enforcing Permissions in Views
Views are protected using the `@permission_required` decorator. For example:
```python
@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, pk):
    # Code for editing book
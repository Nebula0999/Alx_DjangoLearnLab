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
    # Security Measures Implemented in LibraryProject

## Configured Settings
- **DEBUG set to False**: Ensures that sensitive error information is not exposed in production.
- **CSRF_COOKIE_SECURE and SESSION_COOKIE_SECURE**: Prevent cookies from being sent over non-HTTPS connections.
- **Content Security Policy (CSP)**: Restricts the sources of content to mitigate XSS attacks.
- **X_FRAME_OPTIONS set to 'DENY'**: Protects against clickjacking attacks.

## View Security
- All user input is processed using Django’s ORM to avoid SQL injection.
- Views that handle forms include `{% csrf_token %}` to safeguard against CSRF attacks.

## Testing Approach
1. Manually tested all input forms to ensure CSRF tokens are present.
2. Checked CSP by inspecting browser console logs for violations.
3. Validated that forms are protected against XSS by submitting malicious scripts and confirming they are sanitized.
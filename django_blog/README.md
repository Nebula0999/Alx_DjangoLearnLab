# Django Blog Authentication System

## Features
1. **User Registration**:
   - Users can register with a username, email, and password.
2. **Login/Logout**:
   - Secure login and logout functionality.
3. **Profile Management**:
   - Users can view and update their email address.

## URLs
1. `/register/`: Register a new account.
2. `/login/`: Log in to your account.
3. `/logout/`: Log out of your account.
4. `/profile/`: View and update your profile.

## Security
- CSRF tokens are used in all forms.
- Passwords are hashed using Django's secure password hashing algorithms.

## How to Test
1. Run the Django development server:
   ```bash
   python manage.py runserver
1. **CRUD Operations**:
   - List all posts (`/posts/`).
   - View a single post (`/posts/<id>/`).
   - Create a post (`/posts/new/`).
   - Edit a post (`/posts/<id>/edit/`).
   - Delete a post (`/posts/<id>/delete/`).

2. **Permissions**:
   - Authenticated users can create posts.
   - Only post authors can edit or delete their posts.
# Comment System

## Features
1. Add comments to blog posts.
2. Edit and delete comments (authors only).
3. Display all comments under each blog post.

## URLs
- `/posts/<post_id>/comments/new/`: Add a new comment.
- `/comments/<comment_id>/edit/`: Edit a comment.
- `/comments/<comment_id>/delete/`: Delete a comment.

## Permissions
- Authenticated users can add comments.
- Only comment authors can edit or delete their comments.

## Testing
1. Test adding, editing, and deleting comments.
2. Verify that unauthorized users cannot perform restricted actions.
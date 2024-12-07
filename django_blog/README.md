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
# Tagging and Search Features

## Tagging
1. Tags can be added to blog posts during creation or editing.
2. Each post detail page displays its associated tags.
3. Clicking on a tag shows all posts with that tag.

## Search
1. Use the search bar to find posts by title, content, or tags.
2. Results are displayed on a separate search results page.

## URLs
- `/search/`: Search posts by keywords.
- `/tags/<tag_name>/`: View posts associated with a specific tag.

## Testing
1. Create a post with tags.
2. Verify the tags are displayed correctly.
3. Test the search bar with various queries to ensure accurate results.
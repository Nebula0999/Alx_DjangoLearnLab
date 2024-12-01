# Advanced API Project

## API Endpoints
1. **GET /books/**: Retrieve a list of all books (public access).
2. **GET /books/<id>/**: Retrieve details of a specific book (public access).
3. **POST /books/create/**: Create a new book (authenticated users only).
4. **PUT /books/<id>/update/**: Update an existing book (authenticated users only).
5. **DELETE /books/<id>/delete/**: Delete a book (authenticated users only).

## Permissions
- **Unauthenticated users**: Can read data (ListView, DetailView).
- **Authenticated users**: Can create, update, and delete books.

## Testing
Use tools like Postman or curl to interact with the API. Ensure proper tokens are passed in the `Authorization` header for write operations.
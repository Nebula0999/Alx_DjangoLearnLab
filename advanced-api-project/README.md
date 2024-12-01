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
# API Enhancements: Filtering, Searching, and Ordering

## Features
1. **Filtering**:
   - Filter books by title, author name, or publication year.
   - Examples:
     - `/books/?title=Harry Potter`
     - `/books/?author__name=J.K. Rowling`
     - `/books/?publication_year=1997`

2. **Searching**:
   - Perform text searches on book titles or author names.
   - Examples:
     - `/books/?search=Harry`
     - `/books/?search=Rowling`

3. **Ordering**:
   - Sort books by title or publication year.
   - Examples:
     - `/books/?ordering=title` (Ascending)
     - `/books/?ordering=-publication_year` (Descending)

## Testing
Use tools like Postman or curl to test the API endpoints with various query parameters.
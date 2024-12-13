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
### Deliverables
1. **Test File**:
   - `/api/test_views.py` includes comprehensive tests for CRUD operations and advanced features.
2. **Testing Outputs**:
   - All tests pass with correct response status codes and data integrity.
3. **Documentation**:
   - Code comments in `test_views.py`.
   - Detailed testing instructions in `README.md`.

This setup ensures your API is robust, secure, and behaves as expected under various conditions.
# API Testing for advanced_api_project

## Overview
This project includes unit tests for the `Book` model API endpoints, ensuring they function as expected under various conditions.

## Test Coverage
1. **CRUD Operations**:
   - Create, Read, Update, and Delete books.
   - Verify status codes and response data integrity.

2. **Advanced Features**:
   - Filter books by title, author, or publication year.
   - Search books by keywords.
   - Order books by title or publication year.

3. **Authentication and Permissions**:
   - Ensure unauthenticated users can only read data.
   - Restrict write operations to authenticated users.

## How to Run Tests
1. Ensure the testing environment is set up with the required dependencies.
2. Run the test suite:
   ```bash
   python manage.py test api

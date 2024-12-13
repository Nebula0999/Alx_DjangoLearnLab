# CustomUser Model
The customeUser model utilizes AbstractUser model to assign fields to the user model with additional bio, profile_picture and followers models

# Setup process
The setup process involved starting a new django project named social_media_api.
Then started a new app called accounts
I configured my accounts app and rest_framework into the installed apps in the settings file
I then set up my custom user model, added seializers and views for my pages.
Then configured the urls in accounts.urls file and urls file

# User Registration
The model utilizes the AbstractUser model to assign fields for user input nad registration

# User Login
To login the user requests for an authentication token
The model uses the tokens to assign permissions to users and allow them to access the page

### Posts API
- **List Posts:** `GET /api/posts/posts/`
- **Create Post:** `POST /api/posts/posts/` (Authenticated)
- **Retrieve Post:** `GET /api/posts/posts/{id}/`
- **Update Post:** `PUT/PATCH /api/posts/posts/{id}/` (Author only)
- **Delete Post:** `DELETE /api/posts/posts/{id}/` (Author only)

### Comments API
- **List Comments:** `GET /api/posts/comments/`
- **Create Comment:** `POST /api/posts/comments/` (Authenticated)
- **Retrieve Comment:** `GET /api/posts/comments/{id}/`
- **Update Comment:** `PUT/PATCH /api/posts/comments/{id}/` (Author only)
- **Delete Comment:** `DELETE /api/posts/comments/{id}/` (Author only)

### Filtering and Pagination
- **Filter Posts:** Add query parameters `?search={query}` for title or content.
- **Pagination:** Add query parameters `?page={page_number}`.

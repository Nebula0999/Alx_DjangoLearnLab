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

### Follow and Unfollow Endpoints
- **Follow a User:** `POST /api/accounts/follow/<user_id>/`
  - Requires authentication.
  - Response:
    ```json
    {
      "message": "You are now following <username>"
    }
    ```

- **Unfollow a User:** `POST /api/accounts/unfollow/<user_id>/`
  - Requires authentication.
  - Response:
    ```json
    {
      "message": "You have unfollowed <username>"
    }
    ```

### Feed Endpoint
- **Get the Feed:** `GET /api/posts/feed/`
  - Requires authentication.
  - Response:
    ```json
    [
      {
        "id": 1,
        "author": "<username>",
        "title": "Post Title",
        "content": "Post Content",
        "created_at": "<timestamp>",
        "updated_at": "<timestamp>",
        "comments": []
      }
    ]
    ```

### Notes on Following and Feed:
- Users cannot follow themselves.
- The feed only shows posts from users that are currently followed.
- Posts are ordered by their creation date, newest first.

### Likes API
- **Like a Post:** `POST /api/posts/<post_id>/like/`
- **Unlike a Post:** `POST /api/posts/<post_id>/unlike/`

### Notifications API
- **List Notifications:** `GET /api/notifications/`
- **Mark Notification as Read:** `POST /api/notifications/<notification_id>/read/`

### Features
- Notifications are generated for:
  - Likes on posts
  - New followers (can be added later)
  - Comments (extendable)

# Deployment Instructions

## Hosting Service
- **Service:** AWS Elastic Beanstalk
- **URL:** [your-app-name.elasticbeanstalk.com](http://your-app-name.elasticbeanstalk.com)

## Environment Variables
- `DEBUG`: `False`
- `SECRET_KEY`: `your-production-secret-key`
- `RDS_DB_NAME`, `RDS_USERNAME`, `RDS_PASSWORD`, `RDS_HOSTNAME`, `RDS_PORT`: Database credentials.

## Deployment Steps
1. Install AWS CLI and EB CLI.
2. Initialize Elastic Beanstalk environment:
   ```bash
   eb init

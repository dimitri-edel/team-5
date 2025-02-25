[team5-api-eu](https://team5-api-eu-5d24fa110c36.herokuapp.com/)

The API endpoint is hosted at https://team5-api-eu-5d24fa110c36.herokuapp.com/ for both the API and frontend.

`team5-api-eu` is VALID APP NAME.
`team5-frontend-eu` is DISCONTINUED.

In development, the URL is http://127.0.0.1:8000/

API is hosted in /api/
Frontend in root /

API endpoints (initial):

| Endpoint | Method | Expect | Result Dev | Result Prod |
|----------|--------|---------|------------|-------------|
| /api/    | GET    | Returns Hello World | ✅ | ❌  |

FRONTEND TESTING:
| Endpoint | Method | Expect | Result Dev | Result Prod |
|----------|--------|---------|------------|-------------|
| /        | GET    | Returns Hello World in frontend React Portal | ✅ | ✅ |



❌* API PROD reveals the frontend. with the following console log outputs

# API Endpoints

| Endpoint                  | Method | Payload                                                                 | Response                                                                 |
|---------------------------|--------|-------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `/like/<int:pk>/`         | POST   | `{}`                                                                   | `201 Created` or `204 No Content` if unliked, `404 Not Found` if not found |
| `/notifications/`         | GET    | N/A                                                                    | List of notifications about received likes                               |
| `/liked-profiles/`        | GET    | N/A                                                                    | List of primary keys of profiles that the user has liked                 |
| `/rest_login/`            | POST   | `{"username": "testeruser", "password": "strongpassword123"}`           | `200 OK` with authentication token                                       |
| `/rest_logout/`           | POST   | N/A                                                                    | `200 OK`                                                                 |
| `/rest_register/`         | POST   | `{"username": "newuser", "email": "newuser@example.com", "password1": "password", "password2": "password"}` | `201 Created` with user details                                          |
| `/userprofile/`           | GET    | N/A                                                                    | List of user profiles                                                    |
| `/userprofile/<int:pk>/`  | GET    | N/A                                                                    | Details of a specific user profile                                       |
| `/userprofile/<int:pk>/`  | PUT    | `{"display_name": "Updated Name", "birth_date": "1990-01-01", ...}`     | `200 OK` with updated profile details                                    |
| `/userprofile/<int:pk>/`  | DELETE | N/A                                                                    | `204 No Content`                                                         |
| `/match/`                 | GET    | N/A                                                                    | List of matches                                                          |
| `/match/<int:pk>/`        | GET    | N/A                                                                    | Details of a specific match                                              |
| `/match/<int:pk>/`        | DELETE | N/A                                                                    | `204 No Content`                                                         |
| `/dislike/<int:pk>/`      | POST   | `{}`                                                                   | `201 Created` or `204 No Content` if undisliked, `404 Not Found` if not found |
| `/disliked-profiles/`     | GET    | N/A                                                                    | List of primary keys of profiles that the user has disliked              |
| `/supabase/health/`       | GET    | N/A                                                                    | Health status of the Supabase service                                    |
| `/supabase/message/`      | GET    | N/A                                                                    | API message from Supabase                                                |
| `/supabase/jwt/`          | POST   | `{"username": "testeruser", "password": "strongpassword123"}`           | `200 OK` with JWT token                                                  |
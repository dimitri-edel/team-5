<<<<<<< HEAD
Deployment issues: 

Expecting the API to be hosted on `https://team5-api-eu-5d24fa110c36.herokuapp.com/api/`

Expecting the frontend to be hosted on `https://team5-api-eu-5d24fa110c36.herokuapp.com/`


--- 

The Frontend is hosted on `https://team5-frontend-eu-5d24fa110c36.herokuapp.com/`

But the API instead hosts the frontend on `https://team5-api-eu-5d24fa110c36.herokuapp.com/api`


---

=======
# Deployment issues: '/api' route reveals the frontend instead of the API.

Expecting the frontend to be hosted on `https://team5-api-eu-5d24fa110c36.herokuapp.com/`

Expecting the API to be hosted on the same URL as the frontend with `/api` as the route.


## Endpoints Overview:

| Endpoint | Method | Expect | Result Dev | Result Prod |
|----------|--------|---------|------------|-------------|
| /        | GET    | Renders Hello World within frontend React Portal | ✅ | ✅(1) |
| /api/    | GET    | Returns Hello World in REST API | ✅ | ❌(2)  |


(1)Frontend Prod does not connect to the API, but that's not the issue for now, the issue is that the API is hosting the frontend.

---

(2) **/api route reveals the frontend instead of the API.** with the following console log outputs

```
Current environment: production

index.Cw4utQlC.js:45 Using API URL: https://team5-api-eu-5d24fa110c36.herokuapp.com/api/

api:1  Access to XMLHttpRequest at 'https://team5-api-eu-5d24fa110c36.herokuapp.com/api/' from origin 'https://team5-api-eu-5d24fa110c36-a80e73224403.herokuapp.com' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.
index.Cw4utQlC.js:45  API Error Details: {message: 'Network Error', response: undefined, status: undefined, headers: undefined}
[...]
            
GET https://team5-api-eu-5d24fa110c36.herokuapp.com/api/ net::ERR_FAILED 200 (OK)
```

## Problem files to review:

**One theory is that these files are somehow overriding the settings, although the solution won't be to use Django Templates.**
Procfile

**Another theory is that these files are somehow overriding the settings, which would explain why the frontend is hosted on the API's URL.**

frontend/vite.config.js
frontend/server.js


**It could also be that the Procfile is somehow overriding the settings, although the solution won't be to use Django Templates.**
rest_api/settings.py

## Debugging Steps

### 1. Procfile

>>>>>>> d6c7b66bdf237225d723e17f22da09cc3dc792e2
deployment is managed by `Procfile` in the root directory

```
web: cd frontend; npm install; npm run build; npx serve dist -s -l $PORT --single
api: gunicorn rest_api.wsgi:application --log-file -
```


The Procfile shows two processes:
web: Handles the frontend by installing dependencies, building the React app, and serving it using npx serve
api: Handles the Django backend using gunicorn


with the command `git push heroku main`

<<<<<<< HEAD
---

need to review the `Procfile` and `settings.py` to ensure that the API and frontend are hosted in the correct places.


---
=======
```
remote: -----> Discovering process types
remote:        Procfile declares types -> api, web
```

It appears from the logs that both the frontend and backend are indeed handled by the Procfile.

### 2. rest_api/urls.py

This file is the main URL configuration for the Django REST API and has a very simple purpose.
>>>>>>> d6c7b66bdf237225d723e17f22da09cc3dc792e2
```python
"""rest_api URL Configuration
    IMPORTANT: urls.py should not handle static files.
"""

from django.contrib import admin
from django.urls import path
from rest_api import views

urlpatterns = [
    path('api/', views.HelloWorld.as_view(), name='hello-world'), # expecting this to be hosted on https://team5-api-eu-5d24fa110c36.herokuapp.com/api/ ISSUE:currently this URL hosts the frontend
    path('admin/', admin.site.urls),
]
```

<<<<<<< HEAD
http://127.0.0.1:8000/api/ works as expected, serves the API.



=======
http://127.0.0.1:8000/api/ works completelyas expected, serves the API, but is overridden in production.


### 3. Modified Procfile to include SCRIPT_NAME:
```
web: cd frontend; npm install; npm run build; npx serve dist -s -l $PORT --single
api: gunicorn rest_api.wsgi:application --bind 0.0.0.0:$PORT --log-file - --env SCRIPT_NAME=/api
```

This was supposed to separate the frontend and backend, but it didn't work.

### 4. Modified settings.py to include SCRIPT_NAME:

```python
// ... existing code ...

# Update STATIC_URL to avoid conflicts with frontend
STATIC_URL = '/api/static/'

# Ensure API paths are correct
FORCE_SCRIPT_NAME = '/api'
// ... existing code ...

```

This was supposed to separate the frontend and backend, but it didn't work. Same EM.

### 5. Identified that `npx serve` in production doesn't match development environment (which uses Vite).
Modified Procfile to use Vite's preview server instead:

```
web: cd frontend; npm install; npm run build; npm run preview -- --host 0.0.0.0 --port $PORT
api: gunicorn rest_api.wsgi:application --bind 0.0.0.0:$PORT --log-file - --env SCRIPT_NAME=/api
```

Rationale: Development uses `npm run dev` with Vite, so production should use Vite's preview server for consistency.

### 6. Simplified Procfile to use only deploy API


```
web: gunicorn rest_api.wsgi:application --log-file -
```

Since there is issues with frontend overriding the API, we can just deploy the API without the frontend. The rationale is to determine that the api is not the issue.
>>>>>>> d6c7b66bdf237225d723e17f22da09cc3dc792e2

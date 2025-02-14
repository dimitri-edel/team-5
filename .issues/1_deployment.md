Deployment issues: 

Expecting the API to be hosted on `https://team5-api-eu-5d24fa110c36.herokuapp.com/api/`

Expecting the frontend to be hosted on `https://team5-api-eu-5d24fa110c36.herokuapp.com/`


--- 

The Frontend is hosted on `https://team5-frontend-eu-5d24fa110c36.herokuapp.com/`

But the API instead hosts the frontend on `https://team5-api-eu-5d24fa110c36.herokuapp.com/api`


---

deployment is managed by `Procfile` in the root directory

```
web: cd frontend; npm install; npm run build; npx serve dist -s -l $PORT --single
api: gunicorn rest_api.wsgi:application --log-file -
```


The Procfile shows two processes:
web: Handles the frontend by installing dependencies, building the React app, and serving it using npx serve
api: Handles the Django backend using gunicorn


with the command `git push heroku main`

---

need to review the `Procfile` and `settings.py` to ensure that the API and frontend are hosted in the correct places.


---
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






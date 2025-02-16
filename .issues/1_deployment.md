# Deployment Issues and Flow with API Production

## 1. API Production Issues

- Development API works: ✅ Returns `{"message":"API is working!"}` at `http://localhost:8000/test/` & `http://localhost:5173/api/test`
- Production API fails: ❌ Returns `{"error":"Failed to fetch from API"}` at `https://team5-api-eu-5d24fa110c36.herokuapp.app/api/test`

## 2. Deployment Flow

1. **Git Push to Heroku**
   ```bash
   git push heroku main
   ```

2. **Procfile Execution**
   - `web-backend`: Runs Django using gunicorn
   - `web`: Runs Node.js frontend server

```
web-backend: gunicorn backend.rest_api.wsgi:application --log-file -
web: node frontend/server.js
```

3. **Backend Deployment**
   - Django app served by Gunicorn
   - Static files handled by WhiteNoise
   - Database migrations run automatically
   - API hosted at `/api` prefix

see urls.py for API endpoints

```py
urlpatterns = [
    path('', RedirectView.as_view(url='test/', permanent=False), name='index'),
    path('test/', views.APITest.as_view(), name='api-test'), # this is the API endpoint
]
```

4. **Frontend Deployment**
   - Node.js server starts
   - Serves built React app
   - Proxies API requests to backend

## 3. Testing Steps

1. Make desired changes to the code
2. Run automated tests

```powershell
cd backend; python3 manage.py test
```

```powershell
cd frontend; npm run test
```

```
 PASS  src/__tests__/api.test.js
  API Tests
    √ should return correct message from direct API endpoint /api/test (3 ms)
    √ should return correct message from frontend proxy endpoint localhost:5173/api/test (1 ms)

```

3. Test production build without committing:
   ```powershell
   heroku git:remote -a team5-api-eu
   git push heroku main -f
   ```


4. Test deployed endpoints:
   ```powershell
   curl https://team5-api-eu-5d24fa110c36.herokuapp.com/api/test/
   ```

5. check logs:

```powershell
heroku logs --tail
```

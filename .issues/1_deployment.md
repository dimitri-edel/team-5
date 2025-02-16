# Deployment Issues and Flow

## 1. API Production Issues

### Current Status
- Development API works: ✅ Returns `{"message":"API is working!"}` at `http://localhost:8000/test/` & `http://localhost:5173/api/test`
- Production API fails: ❌ Returns `{"error":"Failed to fetch from API"}` at `https://team5-api-eu-5d24fa110c36.herokuapp.app/api/test`

### Identified Issues

1. **URL Configuration Mismatch**
   - Frontend is trying to access `/api/test` but backend routes to `/test/`
   - Backend URLs are not properly prefixed with `/api/` in production

2. **CORS Configuration**
   - Production CORS settings may be too restrictive
   - Current CORS settings in `settings.py` only allow specific origins

3. **Proxy Configuration**
   - Frontend server proxy in `server.js` may be incorrectly handling API paths
   - Double `/api` prefix issue in URL construction

4. **Environment Configuration**
   - Inconsistent API base URL usage between development and production
   - Multiple places defining API URLs (frontend components, services, server)

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
   git push heroku main -f
   ```


4. Test deployed endpoints:
   ```powershell
   curl https://team5-api-eu-5d24fa110c36.herokuapp.com/api/test/
   ```
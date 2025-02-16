# Testing Documentation

## Environment URLs

- **Production**: `https://team5-api-eu-5d24fa110c36.herokuapp.app/` (both API and frontend)
- **Development**: `http://127.0.0.1:8000/`

## Application Structure
- API is hosted in `/api`
- Frontend is hosted in root `/`

## 1. Backend Development (Python Server)

check the slack channel for `backend/rest_api/env.py `file which should be in the backend/rest_api/env.py 

### Prerequisites
```bash
cd backend; pip install -r requirements.txt
```

### Start Server
```bash
cd backend; python3 manage.py runserver
```

### Endpoints

| Endpoint | Method | Expected Response | Development Result |
|----------|---------|------------------|-------------------|
| `/` | GET | redirect to test | ✅ `{"message":"API is working!"}` |
| `/test` | GET | Returns API TEST | ✅ `{"message":"API is working!"}` |

## 2. Frontend Development

### Prerequisites
```bash
cd frontend; npm install; npm run build
```

### Start Development Server
```bash
cd frontend; npm run dev
```

### Endpoints

| Endpoint | Method | Expected Response | Development Result | Production Result |
|----------|---------|------------------|-------------------|-------------------|
| `/` | GET | Returns Auth view in frontend | ✅ (2 EMs, 2 warnings) | ✅ |
| `/SignIn` | GET | Returns SignIn | ✅ | ✅ |
| `/SignUp` | GET | Returns SignIn | ✅ | ✅ |
| `/SignUp` | POST | Creates user in DB | no action | no action |

## 3. API in Frontend

### Endpoints

| Endpoint | Method | Expected Response | Development Result | Production Result |
|----------|---------|------------------|-------------------|-------------------|
| `/test` | GET | Returns API TEST | ✅ `{"message":"API is working!"}` | ❌ `{"error":"Failed to fetch from API"}` |

### Main URLs

- Development Frontend: `http://localhost:5173/`
- Development API: `http://localhost:5173/api` & `http://localhost:5173/api`

- Production Frontend: `https://team5-api-eu-5d24fa110c36.herokuapp.app`
- Production API: `https://team5-api-eu-5d24fa110c36.herokuapp.app/api`
# Testing Documentation

## Environment URLs

- **Production**: `https://team5-api-eu-5d24fa110c36.herokuapp.app/` (both API and frontend)
- **Development**: 
  - `http://127.0.0.1:8000/` (API only)
  - `http://localhost:5173/` (frontend)
  - `http://localhost:5173/api` (API proxy)

## Application Structure
- API is hosted in `/api`
- Frontend is hosted in root `/`

# 1: DEVELOPMENT LAYER

all tests must pass in development

## 1.1. Backend Development (Python Server)

check the slack channel for `backend/rest_api/env.py `file which should be in the backend/rest_api/env.py 

### Prerequisites
```bash
cd backend; pip install -r requirements.txt
```

### Start Server
```bash
cd backend; python3 manage.py runserver
```

## 1.2. Frontend Development

### Prerequisites
```bash
cd frontend; npm install; npm run build
```

### Start Development Server
```bash
cd frontend; npm run dev
```

### Development Layer Endpoints

| Layer | URL | Endpoint | Method | Expected Response | Development Result |
|----------|---------|------------------|-------------------|-------------------|-------------------|
| Backend | `http://127.0.0.1:8000/` | `/` | GET | redirect to test | ✅ `{"message":"API is working!"}` | 
| Backend | `http://127.0.0.1:8000/` | `/test` | GET | Returns API TEST | ✅ `{"message":"API is working!"}` |
| | | | | | |
| Frontend | `http://localhost:3000/` |`/` | GET | Returns Auth view in frontend | ✅ (2 EMs, 2 warnings) | 
| Frontend | `http://localhost:3000/` | `api/test` | GET | Returns API call `{"message":"API is working!"}` | ✅ `{"message":"API is working!"}` |
| | | | | | |
| | | | | | |
| Frontend | `http://localhost:3000/` | `/SignIn` | GET | Returns SignIn | ✅ | 
| Frontend | `http://localhost:3000/` | `/SignUp` | GET | Returns SignIn | ✅ | 
| Frontend | `http://localhost:3000/` | `/SignUp` | POST | Creates user in DB | no action | no action |



## 2. PRODUCTION LAYER

### Prerequisites

use `git push main` to deploy to production

### Production Layer Endpoints

| Layer | URL | Endpoint | Method | Expected Response | Production Result |
|----------|---------|------------------|-------------------|-------------------|-------------------|
| Backend | `https://team5-api-eu-5d24fa110c36.herokuapp.app/` | `/` | GET | redirect to test | ❌ |
| Backend | `https://team5-api-eu-5d24fa110c36.herokuapp.app/` | `/test` | GET | Returns API TEST | ❌ |


# Automated Testing

## Unit Testing

```bash
cd backend; python3 manage.py test
```

## Integration Testing

```bash
cd frontend; npm run test
```

## E2E Testing

```bash
cd frontend; npx run playwright test --ui
```

## Manual Testing

```bash


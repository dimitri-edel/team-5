web: cd frontend; npm install; npm run build; npm run preview -- --host 0.0.0.0 --port $PORT
api: gunicorn rest_api.wsgi:application --bind 0.0.0.0:$PORT --log-file - --env SCRIPT_NAME=/api

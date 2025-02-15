web: cd frontend; npm install; npm run build; npx serve dist -s -l $PORT --single
api: gunicorn rest_api.wsgi:application --bind 0.0.0.0:$PORT --log-file - --env SCRIPT_NAME=/api

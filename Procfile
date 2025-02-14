web: cd frontend; npm install; npm run build; npx serve dist -s -l $PORT --single
api: gunicorn rest_api.wsgi:application --log-file -

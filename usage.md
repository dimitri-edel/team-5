# Deployment

there should be a Procfile in the root directory to run the frontend and backend - there should NOT be a Procfile in the frontend directory.


deployment is done through heroku with the following commands:

```bash
heroku login
heroku git:remote -a team5-api-eu
git push heroku main
```

heroku logs can be used to view the logs of the deployed application.

```bash
heroku logs --tail
```







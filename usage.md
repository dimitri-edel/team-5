# Deployment

there should be a Procfile in the root directory to run the frontend and backend - there should NOT be a Procfile in the frontend directory.

we deploy to https://team5-api-eu-5d24fa110c36.herokuapp.com/

`team5-api-eu` is VALID APP NAME.
`team5-frontend-eu` is DISCONTINUED.

## setup
deployment is done through heroku with the following commands:

```bash
heroku login
heroku git:remote -a team5-api-eu
```

## deployment commands

deployment is handled separately for the api and the frontend, although they are in the same repository and sent to the same heroku app in `/api` and `/` respectively.

```bash
# Single deployment command for both frontend and API
git push heroku main
```

heroku logs can be used to view the logs of the deployed application.

```bash
heroku logs --tail
```







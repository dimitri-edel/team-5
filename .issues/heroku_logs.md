Application Logs
2025-02-16T20:03:36.558369+00:00 app[web.1]: Python buildpack: Detected 512 MB available memory and 8 CPU cores.
2025-02-16T20:03:36.559108+00:00 app[web.1]: Python buildpack: Defaulting WEB_CONCURRENCY to 2 based on the available memory.
2025-02-16T20:03:36.756724+00:00 app[web.1]: Frontend server is running on port 42756
2025-02-16T20:03:36.756874+00:00 app[web.1]: Serving static files from: /app/frontend/dist
2025-02-16T20:03:37.118692+00:00 heroku[web.1]: State changed from starting to up
2025-02-16T20:03:46.000000+00:00 app[api]: Build succeeded
2025-02-16T20:05:06.849030+00:00 app[web.1]: Server error: Error: ENOENT: no such file or directory, stat '/app/frontend/dist/index.html'
2025-02-16T20:05:06.852184+00:00 heroku[router]: at=info method=GET path="/" host=team5-api-eu-5d24fa110c36.herokuapp.com request_id=26894255-fe4b-4c89-9e8a-afb9c6297559 fwd="87.114.88.15" dyno=web.1 connect=0ms service=8ms status=500 bytes=240 protocol=https
2025-02-16T20:05:07.360447+00:00 app[web.1]: Server error: Error: ENOENT: no such file or directory, stat '/app/frontend/dist/index.html'
2025-02-16T20:05:07.361487+00:00 heroku[router]: at=info method=GET path="/favicon.ico" host=team5-api-eu-5d24fa110c36.herokuapp.com request_id=35d4a924-51c4-42d1-a42c-3e0998bdf81f fwd="87.114.88.15" dyno=web.1 connect=0ms service=2ms status=500 bytes=240 protocol=https
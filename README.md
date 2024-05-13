Service model for phishing URL classification model.

```docker build -t ghcr.io/remla24-team-1/model-service:1.0.0 .```
```docker run -it -p8081:8081 --rm ghcr.io/remla24-team-1/model-service:1.0.0```

Example curl command for returning query:

```curl -X POST http://localhost:8081/querymodel -H "Content-Type: application/json" -d '{"urls": ["http://www.asodiaisd.com", "http://test2.com", "http://xxxxxxxx.com"]}'```
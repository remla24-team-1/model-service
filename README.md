# Model service - Backend application

This repo contains the backend that works together with the [app-service](https://github.com/remla24-team-1/app/) frontend. It is versioned by [lib-ml](https://github.com/remla24-team-1/lib-ml). The model to be used is automatically pulled on container creation from the [model-training](https://github.com/remla24-team-1/model-training/) repo.

## To run the backend locally for testing or for developing: 
* First clone the repository using `git clone git@github.com:remla24-team-1/model-service.git` and access it with `cd app`.
* Build the project using `docker build -t ghcr.io/remla24-team-1/model-service:latest .`, and run the built image using `docker run -it -p8081:8081 --rm ghcr.io/remla24-team-1/model-service:latest`.

The service will be hosted at localhost. To access the service, the app frontend image is recommended to be ran. 
The model can also queried directly when ran in this context.
Example curl command for returning query:

```curl -X POST http://localhost:8081/querymodel -H "Content-Type: application/json" -d '{"urls": ["http://www.asodiaisd.com", "http://test2.com", "http://xxxxxxxx.com"]}'```

## Release new image

To release a new docker image, create a git tag with `git tag vX.X.X`, and push that tag using `git push origin tag vX.X.X`. The GitHub workflow will then automatically update the corresponding versions accessible at [packages/app](https://github.com/orgs/remla24-team-1/packages/container/package/model-service).

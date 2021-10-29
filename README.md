# buoy-sre-api challenge

## Summary
This project has been built for development use only.  The Buoy API is a simple comments web API that hosts comments and like endpoints.  Below you will find information related to deployment and use of the product. 

## Prerequisites
This project has been developed and used with Docker Desktop Kubernetes installation.  While it may work outside of this environment, it has not been tested.  If you are deploying to Kubernetes, you must have the ability to run kubectl apply within this environment.

# Deployment methods
## Run locally
Additional requirements can be installed with pip or pip3.
- python 3.6
- Flask-SQLAlchemy
- flask-marshmallow
- marshmallow-sqlalchemy

With all dependencies present, the startup.sh script can be run to start the API.  This will build the database locally, if it does not already exist.

## Docker Run
A deployment script has been provided for simple build and deployment of a locally hosted container.  
1. Verify that docker is running on your system and you have access to public internet. This project pulls from the python base docker image.
2. Clone this repository locally. 
3. From the project directory, run the docker_deploy.sh script to build and deploy the container.
4. The API will be accessable from http://127.0.0.1:5000

## K8s deployment
A deployment script has been provided for simple build and deployment of a Kubernetes cluster.  Please perform the below on your local Kubernetes deployment or system or within a namespace you have access to deploy to. 
1. Verify that docker is running on your system and you have access to public internet. This project pulls from the python base docker image.
2. Clone this repository locally.
3. If you are deploying this within a namespace, you can modify the deployment script to include your namesspace arguments with -n <namespace>.
3. From the project directory, run the K8s_deploy.sh script to build and deploy your container.
4. Notate the NodePort that is supplied at the end of the deployment.  It will be used to access with the below instructions.

## Accessing the API
The API can be accessed via http://localhost{NodePort} or http://127.0.0.1:{NodePort}.  The payload for requests should be in json format and look like the below.

```json
{
    "content": "Comment content",
    "title": "Comment title"
}
```

## API Endpoints
This api has several endpoints that can be seen in the Webapp.py script.  Below is a description of them.  I suggest using an application such as [Postman](http://postman.com "Postman") to perform these tests.
1. POST comment endpoint, "payload required"
    http://127.0.0.1:{NodePort}/comment
2. GET all comments endpoint.
    http://127.0.0.1:{NodePort}/comments
3. GET single comment endpoint.  {id} is the primary key of the comment being requested.
    http://127.0.0.1:{NodePort}/comment/{id}
4. PUT update single comment. "payload required" {id} is the primary key of the comment being requested.
    http://127.0.0.1:{NodePort}/comment/{id}
5. PUT like single comment. {id} is the primary key of the comment being requested.
    http://127.0.0.1:{NodePort}/like/{id}
6. PUT like single comment. {id} is the primary key of the comment being requested.
    http://127.0.0.1:{NodePort}/unlike/{id}
7. DELETE single comment. {id} is the primary key of the comment being requested.
    http://127.0.0.1:{NodePort}/comment/{id}

# Example output from GET requests and like comments

```json
{
    "content": "Comment contents",
    "like": 1,
    "title": "Comment title"
}
```

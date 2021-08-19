# custom-entity-store
A simple CRUD API that lets you store custom entities into a database. Basically a document store with a `type` UUID field to logically separate data of different types.


### Deploying to EKS cluster

This repo contains a containerized Django project that you can deploy to our test EKS cluster. Here are instructions for deploying it:

```
# First, make sure you have AWS credentials configured with access to SinglePlatform account's "SP Dev" user role.

# Get ECR credentials:
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 441286785407.dkr.ecr.us-east-1.amazonaws.com

# Build and tag docker container:
docker build -t custom-entity-store .
docker tag custom-entity-store:latest 441286785407.dkr.ecr.us-east-1.amazonaws.com/custom-entity-store

# Push to ECR:
docker push 441286785407.dkr.ecr.us-east-1.amazonaws.com/custom-entity-store

# Then restart the deployment:
kubectl rollout restart -n test-namespace deployment test-deployment

# To check deployment status:
kubectl -n test-namespace get all

# To check pod status:
kubectl -n test-namespace get pod

# The service will then be deployed to:
# http://k8s-testname-testingr-fc74841668-1801831464.us-east-1.elb.amazonaws.com/v1/example/ping

```

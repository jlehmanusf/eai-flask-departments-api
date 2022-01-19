# EAI Flask Student API

### How to run locally

1. If you don't have Docker Desktop installed then follow the directions on the following
   page: https://usfjira.atlassian.net/wiki/spaces/UHP/pages/20443136005/Docker+Desktop+-+Installation+Mac+OS
2. Create an .env file and set the following:
    1. BANNER_PASSWORD
    2. BANNER_USERNAME
    3. BANNER_INSTANCE
3. Run ```docker-compose up --build```
    1. This builds the image and then runs it.
    2. The application runs in a mode that allows you to make changes to the application without stopping and restarting
       the container. If you change the configuration of the application then you must manually stop and start again.

### Adding new environment variables

1. Add to .env file
2. Then add a reference to the docker-compose.yml file in the environment section.
    1. Example: ```- BANNER_INSTANCE=${BANNER_INSTANCE}```
3. You can hard code any non-secrets in the Dockerfile.prod file.
4. Any secrets would need to be added as a Kubernetes secret to the cluster.








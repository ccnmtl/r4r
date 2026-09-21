# Ready for Residency
- [Ready for Residency](#ready-for-residency)
  - [About the Project](#about-the-project)
  - [Developer - Local Testing and Deployments](#developer---local-testing-and-deployments)
    - [Docker Deployment -- Recommended](#docker-deployment----recommended)
      - [Making changes to the Dockerfile](#making-changes-to-the-dockerfile)
    - [Basic System Deployment](#basic-system-deployment)
      - [Create a Postgres Database](#create-a-postgres-database)
      - [Initiate the runserver](#initiate-the-runserver)
## About the Project
Ready for Residency (R4R) is a 2026 Provost-funded project currently in development at the Center for Teaching and Learning.
## Developer - Local Testing and Deployments
### Docker Deployment -- Recommended
With an active Docker service running and your terminal pointing to the project directory enter the following:
```
docker compose up -d
```
#### Making changes to the Dockerfile
1. After any changes remember to stop the current instance:
    ```
    docker compose down
    ```
2. Prune the current instance:
    ```
    docker builder prune
    ```
3. Create the new build:
    ```
    docker build --no-cache
    ```
### Basic System Deployment
#### Create a Postgres Database
#### Initiate the runserver
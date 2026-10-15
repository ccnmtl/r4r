# Ready for Residency
- [Ready for Residency](#ready-for-residency)
  - [About the Project](#about-the-project)
  - [Developer - Local Testing and Deployments](#developer---local-testing-and-deployments)
    - [Docker Deployment -- Recommended](#docker-deployment----recommended)
      - [Making changes to the Dockerfile](#making-changes-to-the-dockerfile)
    - [Basic System Deployment](#basic-system-deployment)
      - [Prepare the Postgres Database](#prepare-the-postgres-database)
      - [Initiate the server](#initiate-the-server)
    - [Using the Courseworks API](#using-the-courseworks-api)
      - [Create an access token](#create-an-access-token)
      - [Using the Courseworks API key](#using-the-courseworks-api-key)
  - [Using the Ready 4 Residency API](#using-the-ready-4-residency-api)
    - [Navigation](#navigation)
    - [Course Creation](#course-creation)
      - [Finding the Course ID](#finding-the-course-id)
## About the Project
Ready for Residency (R4R) is a 2026 Provost-funded project currently in development at the Center for Teaching and Learning.

The site generates courses, rosters, and instructor lists using CourseWorks data. Courseworks IDs are required for making new courses.
## Developer - Local Testing and Deployments
### Docker Deployment -- Recommended
With an active Docker service running and your terminal pointing to the project directory enter the following:
```
docker compose up -d
```
#### Making changes to the Dockerfile
After any changes remember to stop the current instance:
```
docker compose down
```
Prune the current instance:
```
docker builder prune
```
Create the new build:
```
docker build --no-cache
```
### Basic System Deployment
#### Prepare the Postgres Database
Install postgres onto your system [directly from the site](https://www.postgresql.org/download/) or install using a package manager via your computer's terminal.

Using the terminal, run:
```
createdb r4r
```
Navigate to the project directory and run:
```
./manage.py migrate
``` 
#### Initiate the server
In the project directory run:
```
make runserver
```
In a second tab, run:
```
npm install; npm run dev
```
### Using the Courseworks API
You can access Courseworks data using 
[Instructure's Canvas service](https://developerdocs.instructure.com/services/canvas).
#### Create an access token
1. Go to https://courseworks2.columbia.edu/
2. Click on Account in the left sidebar
3. Scroll down to Approved Integrations and click New Access Token
4. Fill out the form:
   * Purpose: Write something that will make the use clear, particularly since the token will have to be renewed at a later date.
   * Use the latest possible expiration time.
5. Copy the token and store it safely as `COURSEWORKS_API` in the project's local `.env` or in an AWS Parameter Store Secure String. If you lose the key you will have to generate a new one.
6. Testing:
   * Web browser: https://courseworks2.columbia.edu/api/v1/courses?ACCESS_KEY=replace_this_with_the_access_key 
   * Terminal command: 
      ```
      curl https://courseworks2.columbia.edu/api/v1/courses?ACCESS_KEY=replace_this_with_the_access_key
      ```
#### Using the Courseworks API key
Ready 4 Residency uses `axios` for data requests. As a default pages pull at most 1000 items per request. ___All data obtained using the access key is directly connected to the user account.___ So the user access key holder should be a primary stakeholder or administrative developer on the project. 

The primary request will be for enrollments affiliated with specific courses. This will use the following API path: `courses/courseid:/enrollments`

Other useful API paths are available, though some of the paths are are only available using the key holder's user id number:
* `/courses` courses affiliated to the access key holder.
* `/courses/course_id:/enrollments` ___The most relevant data for the project.___ Contains all affiliated users and their roles in the course
* `/courses/course_id:/users` all of the users affiliated with a chosen course.
* `/users/user_id_key_holder_only:` the key holder's user profile data
* `/users/user_id_key_holder_only/courses:` same as `/courses`
* `/users/user_id_key_holder_only/enrollments:` all course enrollment data for the key holder

## Using the Ready 4 Residency API
You must be logged in to access the API. Currently, the API is only accessible to superusers as of now. Go to the `/api/` page to start.
### Navigation
The API can be navigated using the url links between different displays. 
### Course Creation
Courses, new Users, Course Teams, and Rotations are all automatically derived using the ___courseworks_id___. The courseworks id is the course id found in courseworks.
#### Finding the Course ID
1. Log in to https://couseworks2.columbia.edu
2. Click into a course.
3. Look at the url. The number at the end `e.g. /courses/>>12345<<` is the course id.
4. Enter that number into the `Courseworks` input when creating a new course.
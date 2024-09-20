Course Project: Recipe App API

Overview
The Recipe App API is a Django-based backend that allows users to create and manage recipes. It uses a PostgreSQL database and the project is containerized using Docker. The app is deployed on AWS, and the API documentation can be accessed [here](http://ec2-35-91-229-207.us-west-2.compute.amazonaws.com/api/docs/).

Features
User Authentication: Supports user sign-up, login, and token-based authentication.
Recipe Management: Users can create, update, and delete their recipes.
Tagging System: Recipes can be categorized with tags.
Ingredient Management: Users can create and manage recipe ingredients.
Image Uploads: Recipes can have images attached.
API-Driven: RESTful API built using Django Rest Framework.
Technology Stack
Backend: Django, Django REST Framework
Database: PostgreSQL
Containerization: Docker, Docker Compose
Testing: Unit tests with Django's test framework
Deployment: AWS EC2, Nginx
Access the Application
The Recipe App API is deployed and accessible here: http://ec2-35-91-229-207.us-west-2.compute.amazonaws.com/api/docs/

Running Locally
Prerequisites

Ensure you have the following installed:

Docker
Docker Compose
Setup

### Setup

Clone this repository:

```bash
git clone https://github.com/your-username/recipe-app-api.git
cd recipe-app-api
docker-compose up --build
```
Build and start the containers:
```bash
docker-compose up --build
```
The app will be available at http://localhost:8000/.

Running Tests
To run the unit tests:
```bash
docker-compose run app sh -c "python manage.py test"
```
Project Structure 
```bash
.
├── app
│   ├── core
│   ├── recipe
│   ├── users
│   └── manage.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── ...
```


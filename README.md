# Project Title: Recipe Sharing Platform - Backend

## Description

This repository contains the backend code for the Recipe Sharing Platform, built using Django. The backend provides API endpoints for managing recipes and integrates with a React frontend deployed on AWS S3 and CloudFront.

## Features

- RESTful API for recipe management
- User authentication and authorization
- CRUD operations for recipes
- Image handling for recipe images
- PostgreSQL database integration
- Additional endpoints for updating and deleting recipes by name and user ID

## Technologies Used

- Django
- Django Rest Framework
- PostgreSQL
- AWS EC2
- AWS S3
- AWS CloudFront

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/recipe-sharing-backend.git
   cd recipe-sharing-backend
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Setup the PostgreSQL database and update `settings.py`:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_db_name',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'your_db_host',
           'PORT': 'your_db_port',
       }
   }

   ALLOWED_HOSTS = ['your_ec2_public_ipv4']
   ```

5. Run migrations and start the development server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## Deployment on AWS

### Deploying Django Backend on EC2

1. Launch an EC2 instance and SSH into it.
2. Install required software:
   ```bash
   sudo apt update
   sudo apt install python3-pip python3-dev libpq-dev nginx curl
   sudo apt install postgresql postgresql-contrib
   ```
3. Clone the repository and set up the virtual environment:
   ```bash
   git clone https://github.com/yourusername/recipe-sharing-backend.git
   cd recipe-sharing-backend
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
4. Configure PostgreSQL and update `settings.py` as mentioned above.
5. Run migrations:

   ```bash
   python manage.py migrate
   ```

6. Configure Gunicorn:

   ```bash
   pip install gunicorn
   gunicorn --workers 3 --bind unix:/home/ubuntu/recipe-sharing-backend/recipe-sharing-backend.sock wsgi:application
   ```

7. Configure Nginx:

   ```bash
   sudo nano /etc/nginx/sites-available/recipe-sharing
   ```

   Add the following configuration:

   ```nginx
   server {
       listen 80;
       server_name your_server_ip;

       location / {
           include proxy_params;
           proxy_pass http://unix:/home/ubuntu/recipe-sharing-backend/recipe-sharing-backend.sock;
       }
   }
   ```

   Enable the configuration:

   ```bash
   sudo ln -s /etc/nginx/sites-available/recipe-sharing /etc/nginx/sites-enabled
   sudo nginx -t
   sudo systemctl restart nginx
   sudo systemctl restart gunicorn
   ```

### Deploying React Frontend on S3 and CloudFront

1. Build the React project:
   ```bash
   npm run build
   ```
2. Upload the build folder to an S3 bucket:
   ```bash
   aws s3 sync build/ s3://your-s3-bucket-name
   ```
3. Set up CloudFront to serve the S3 bucket content.

## Accessing the API

Use the EC2 instance's public IPv4 address as the backend URL to call the endpoints. For example:

- GET: `http://<ec2_public_ipv4>/api/recipes/`
- POST: `http://<ec2_public_ipv4>/api/recipes/`
- GET: `http://<ec2_public_ipv4>/api/recipes/user/{uid}`
- PUT: `http://<ec2_public_ipv4>/api/recipes/update/<name>/<uid>/`
- DELETE: `http://<ec2_public_ipv4>/api/recipes/delete/<name>/<uid>/`

## License

This project is licensed under the MIT License.

## About Me

I am Dipit Vasdev, a highly motivated problem solver with a passion for neural networks and machine learning. I recently completed my Master's degree in Computer Engineering at New York University, and my greatest strength lies in my drive for solving complex problems in computer science. I possess a wealth of technical skills in machine learning, deep learning, Android development, and more, and I have taken part in various projects and internships to continuously improve my skills and knowledge.

## Links

[LinkedIn](https://www.linkedin.com/in/dipit-vasdev)

## Feedback

If you have any feedback, please reach out to me at [dipit.vasdev@nyu.edu](mailto:dipit.vasdev@nyu.edu).

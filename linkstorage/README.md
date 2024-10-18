API Link Storage

The project provides API to manage collection of links for users.

To launch the project you need the Docker environment on the host machine installed first. The run from the root of the project the following command:

1. Clone the repository:
    ```bash
    cd linkstorage
    ```

2. Build a Docker image:
    ```bash
    docker-compose up --build
    ```

3.Open your browser and go to `http://localhost:8000`.

To see the Swagger documentation open the link: `http://localhost:8000/swagger/`

Main stack:
- Python 3.12+;
- Django 5.0+ (Django Rest Framework);
- Docker v27+;
- db.SQLite3;
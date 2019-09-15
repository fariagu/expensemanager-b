# Django-Postgres-Compose

Template project for future webapps using django as backend, postgres as DB and running inside a docker container

## Instructions

### Python

#### Create a python virtual environment (virutalenv)

First time only.

1. Instal virtualenv (if necessary)

    ``` bash
    pip3 install --user virtualenv
    sudo apt install python3-venv
    ```

2. Create virtual environment named 'env'

    ``` bash
    python3 -m venv env
    ```

#### Activate a virtual environment

``` bash
source env/bin/activate
```

#### Leave virtual environment

``` bash
deactivate
```

### Docker

#### Create Django project

1. Change directory to root of project
2. Create the project by running:

    ``` bash
    sudo docker-compose run web django-admin startproject composedjango .
    ```

3. Change ownership of new files

    ``` bash
    sudo chown -R $USER:$USER .
    ```

#### Connect Database

1. Edit the ```composedjango/settings.py``` file
    1. Add ```'corsheaders'``` to the ```INSTALLED_APPS``` section
    2. Add ```'corsheaders.middleware.CorsMiddleware'``` to the ```MIDDLEWARE``` section
    3. Replace the ```DATABASES = ...``` section with the following:

        ``` python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'postgres',
                'USER': 'postgres',
                'HOST': 'db',
                'PORT': 5432,
            }
        }
        ```

    4. Add ```CORS_ORIGIN_ALLOW_ALL = True``` to the bottom of the file

2. Run the following command from the project root:

    ``` bash
    docker-compose up
    ```

3. Go to <http://localhost:8000> to confirm server is running

#### Notes

Docker daemon must be running

``` bash
sudo service docker start
```

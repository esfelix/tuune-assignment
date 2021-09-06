Tuune Programming Assignment
============================

My solution to the Tuune programming assignment.

![image](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter%0A%20%20:target:%20https://github.com/pydanny/cookiecutter-django/%0A%20%20:alt:%20Built%20with%20Cookiecutter%20Django)

See the public API documentation to learn what the API does and how to interact with it: https://angry-cheetah-32.redoc.ly/


### Running the app

Ensure docker is installed and running.

Run:

```sh
docker compose up
```

Create a test user 

```sh
docker compose run django python manage.py create_random_user
[+] Running 1/0
 ⠿ Container postgres  Running                                                                                                    0.0s
PostgreSQL is available
Username: Michelleovzlt
Token: dacfc280ce6451a56677ead2d5c2d077a398a79c
```

(There is also a makefile which defines a number of shorcuts to interact with the app via the command line).

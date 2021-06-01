Tuune Programming Assignment
============================

My solution to the Tuune programming assignment.

![image](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter%0A%20%20:target:%20https://github.com/pydanny/cookiecutter-django/%0A%20%20:alt:%20Built%20with%20Cookiecutter%20Django)


### Running the app

Ensure docker is installed and running and run:

    $ docker-compose up

See the API docs for details on how to use the API: https://felixes.stoplight.io/docs/tuune-assignment


You can send requests directly from the API docs using the "Try it out" section for the [endpoint](https://felixes.stoplight.io/docs/tuune-assignment/tuune-assignment-api.yaml/paths/~1api~1v1~1income-tax~1calculate/post).

Example requests:

**curl**

```
curl --request POST \
  --url http://localhost:8000/api/v1/income-tax/calculate \
  --header 'Content-Type: application/json' \
  --data '{"income":52000,"show_breakdown":true}'
```

**httpie**

```
echo '{"income":52000,"show_breakdown":false}' |  \
  http POST http://localhost:8000/api/v1/income-tax/calculate \
  Content-Type:application/json
```

#### Running tests with py.test

    $ docker-compose run django pytest

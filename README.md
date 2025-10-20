# Django Advanced Blog


for building:
```
docker build -t django .

```

```
docker run -p 8000:8000 django
```

```
docker-compose up --build
```

for migrating:
```
docker-compose exec backend sh -c "python manage.py makemigratons"
```

for using black reformatter:
```
docker-compose exec backend sh -c "black ."
```

for using flake8
```
docker-compose exec backend sh -c "flake8 ."
```

for testing
```
docker-compose exec backend sh -c "python manage.py test"
```

for testing using pytest
```
docker-compose exec backend sh -c "pytest ."
```

for running the custom insert_data command
```
docker-compose exec backend sh -c "python manage.py insert_data"
```

for using redis cli
```
docker-compose exec -it redis sh
redis-cli
```

for using celery
```
docker-compose exec backend sh -c "celery -A core worker --loglevel=info"
```

for activating celery beat
```
docker-compose exec backend sh -c "celery -A core beat -l info"
```

another command for celery beat
```
docker-compose exec backend sh -c "celery -A core beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler"
```
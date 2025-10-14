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
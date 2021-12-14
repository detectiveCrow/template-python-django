## Run Local Env

### build
```
docker-compose build
```

### run local server
```
docker-compose up -d
```

### create superuser

#### connect to app container
```
docker-compose exec app ./manage.py shell
```

#### create user
```
from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'password')
```
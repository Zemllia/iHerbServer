# iHerbServer

## Развертка

`source venv/bin/activate`  
В файл settings.py прописываем настройки бд  
Например:  
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}
```

Затем  
`python manage.py migrate`
И потом  
`python manage.py runserver`
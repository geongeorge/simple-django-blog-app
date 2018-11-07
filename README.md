# Simple Django Blog App

A simple blog made with django framework and mysql

## 🚀 To Start Server:

Create a database in mysql and edit `settings.py`
```
DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'djangoproject',
        'USER' : 'root',
        'PASSWORD' : '',
        'HOST' : 'localhost',
        'PORT' : ''
    }
}
```

Create a Virtual environment(Optional but recommended)
```
mkvitrualenv envname
```

Install Requirements ⚙️
```
pip install -r requirements.txt
```

Install Migrations
```
python manage.py migrate
```

Run Server 🔥
```
python manage.py runserver
```

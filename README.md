# Django Dairy API

## File structure

```
.
├── api
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__.cpython-38.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-38.pyc
│   │   ├── apps.cpython-38.pyc
│   │   ├── __init__.cpython-38.pyc
│   │   ├── models.cpython-38.pyc
│   │   ├── serialiser.cpython-38.pyc
│   │   ├── urls.cpython-38.pyc
│   │   └── views.cpython-38.pyc
│   ├── serialiser.py
│   ├── templates
│   │   └── api
│   │       └── api_dashboard.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── base
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_auto_20210624_1344.py
│   │   ├── 0003_auto_20210628_0838.py
│   │   ├── 0004_auto_20210628_1414.py
│   │   ├── 0005_alter_text_created_at.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-38.pyc
│   │       ├── 0002_auto_20210624_1344.cpython-38.pyc
│   │       ├── 0003_auto_20210628_0838.cpython-38.pyc
│   │       ├── 0004_auto_20210628_1414.cpython-38.pyc
│   │       ├── 0005_alter_text_created_at.cpython-38.pyc
│   │       └── __init__.cpython-38.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-38.pyc
│   │   ├── apps.cpython-38.pyc
│   │   ├── __init__.cpython-38.pyc
│   │   ├── models.cpython-38.pyc
│   │   ├── urls.cpython-38.pyc
│   │   └── views.cpython-38.pyc
│   ├── serializer.py
│   ├── static
│   │   └── img
│   │       ├── happiness.jpg
│   │       └── home.svg
│   ├── templates
│   │   └── base
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── includes
│   │       │   └── messages.html
│   │       ├── login.html
│   │       ├── profile.html
│   │       ├── register.html
│   │       ├── text_confirm_delete.html
│   │       ├── text_detail.html
│   │       ├── text_form.html
│   │       └── text_list.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── commands.txt
├── data
│   └── clean_data.csv
├── data.py
├── db.sqlite3
├── diaryapi
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   ├── settings.cpython-38.pyc
│   │   ├── urls.cpython-38.pyc
│   │   └── wsgi.cpython-38.pyc
│   ├── settings.py
│   ├── templates
│   ├── urls.py
│   └── wsgi.py
├── dl-model
│   └── lr_combined_tfidf.bin
├── docs
├── manage.py
├── protected
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__.cpython-38.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-38.pyc
│   │   ├── apps.cpython-38.pyc
│   │   ├── __init__.cpython-38.pyc
│   │   ├── models.cpython-38.pyc
│   │   ├── urls.cpython-38.pyc
│   │   └── views.cpython-38.pyc
│   ├── templates
│   │   └── protected
│   │       ├── base.html
│   │       ├── login_admin.html
│   │       ├── profile_admin.html
│   │       ├── profile_text_detail.html
│   │       └── protected.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── README.md
└── requirement.txt
```

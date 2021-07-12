# Django Dairy API

# Contexte

Vous travaillez pour une ESN. Un client vous demande de développer pour lui une application web.

Votre client est un coach de vie, il aide les personnes a se sentir bien dans leur quotidien. Pour suivre le moral de ses clients en deux séances de coaching, il leur demande d'écrire tous les jours un petit texte.

Il y a quelque temps, un influenceur a conseillé ce coach à sa communauté, il est depuis totalement débordé et a eu l'idée d'un outil numérique pour automatiser son suivi. (ppff les coachs...)

Vous devez donc construire et publier:

* une base de données pour stocker les informations de votre coach
* une API REST avec fastAPI (ou autre) pour pouvoir intéagir avec cette base de données
* une application web avec streamlit (ou autre) utilisée comme interface grafique.

Ce qu'un client (du coach) doit pouvoir faire:

* ajouter un texte à la date du jour
* modifier un texte à la date du jour
* lire son texte à la date du jour ou à n'importe quelle date

Ce que le coach doit pouvoir faire:

* ajouter/supprimer/renommer un client.
* ajouter/supprimer/modifier certaines informations sur le client.
* obtenir la liste de tous ses clients et les informations stockées sur lui.
* pour un certain client à une certaine date obtenir le texte d'une client, son sentiment majoritaire, sa roue des émotions (% de chaque sentiment)
* Pour un certain client, un certain jour, une certaine semaine, un certain mois ou une certaine année: récupérer la roue des sentiments moyenne sur la période
* Pour un certain jour, une certaine semaine, un certain mois, une certaine année: récupérer la roue des sentiments moyennes de l'ensemble de ses clients sur la période

# API endpoints

Load the API schema, it will display all of the API endpoints
```
$ coreapi get http://127.0.0.1:8000/docs/
```
API endpoints for the **Text entity**:

texts > list GET
```
/api/texts/
```
texts > create POST
```
/api/texts/
```

texts > read GET
```
/api/texts/{id}
```

texts > update PUT
```
/api/texts/{id}
```

texts > delete DELETE
```
api/texts/{id}
```

API endpoints for the **User entity**:

users > list GET
```
/api/users/
```
users > create POST
```
/api/users/
```

users > read GET
```
/api/users/{id}
```

users > update PUT
```
/api/users/{id}
```

users > delete DELETE
```
api/users/{id}
```


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

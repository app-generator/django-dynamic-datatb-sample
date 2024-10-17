# [Django Dynamic DT](https://github.com/app-generator/django-dynamic-datatb) `Sample`

This project is a free sample that implements [Django Dynamic DataTables](https://github.com/app-generator/django-dynamic-datatb) from scratch. 

<br /> 

---

> For a **complete set of features** and long-term support, check out **[Dynamic Django](https://app-generator.dev/docs/developer-tools/dynamic-django/index.html)**, a powerful starter that incorporates the following:

- ✅ [Dynamic DataTables](https://app-generator.dev/docs/developer-tools/dynamic-django/datatables.html): using a single line of configuration, the data saved in any table is automatically managed
- ✅ [Dynamic API](https://app-generator.dev/docs/developer-tools/dynamic-django/api.html): any model can become a secure API Endpoint using DRF
- ✅ [Dynamic Charts](https://app-generator.dev/docs/developer-tools/dynamic-django/charts.html): extract relevant charts without coding all major types are supported
- ✅ [CSV Loader](https://app-generator.dev/docs/developer-tools/dynamic-django/csv-loader.html): translate CSV files into Django Models and (optional) load the information
- ✅ Powerful [CLI Tools](https://app-generator.dev/docs/developer-tools/dynamic-django/cli.html) for the GIT interface, configuration editing, updating the configuration and database (create models, migrate DB)

<br />

## How to use it

<br />

> 👉 `Download` the code 

```bash
$ git clone https://github.com/app-generator/django-dynamic-datatb-sample.git
$ cd django-dynamic-datatb-sample
```

<br />

> 👉 Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

<br />

> 👉 `Set Up Database`

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> 👉 `Start` the app

```bash
$ python manage.py runserver
```

<br />

At this point, the Dynamic DataTable UI is up & running:

- **Book** Model - `http://127.0.0.1:8000/datatb/books/`. 
- **City** Model - `http://127.0.0.1:8000/datatb/cities/`. 

<br />

![Django Dynamic DataTables - Splash Screen.](https://user-images.githubusercontent.com/51070104/198944457-1ca45c93-2290-484d-ac27-fb77188e61d3.jpg)

<br />

---
[Django Dynamic DataTables](https://github.com/app-generator/django-dynamic-datatb) - Open-source library provided by **[AppSeed](https://appseed.us/)**

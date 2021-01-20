## Plates Direct

### Time

2Hours 30Mins # 17/01/2021 # 10:00pm - 12:30pm
Set up the project.

1Hour 33Mins # 18/01/2021 # 20:40pm - 21:14pm / 13:26pm - 12:25pm
Started on the home page, content and layout.

20/01/2021 # 09:09am - 10:40am / 11:00am - 11:50am / 14:30pm - 
Added the registration input and style. 

Time: 2.5 hours.

### Feature left to implement

- When the user has pressed 'checkout' a promt will appear asking them if they want to add a kitting kit to their basket.

### Django project setup

Creating a virtual environment

   python3 -m venv .venv

Activate the environment

   source .venv/bin/activate

Install django

   pip3 install django

Start a new project

   django-admin startproject PROJECTNAME .

Start a new app

   django-admin startapp APPNAME

Install new app (settings.py)

   INSTALLED_APPS = [
        "django.contrib.staticfiles",
        "APPNAME"
    ]

Import (settings.py)

    import os
    from os import path

Create path to tamplates

   "DIRS": [
            os.path.join(BASE_DIR, "templates")
    ],

Create path to static and media files

    STATIC_URL = "/static/"
    STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")

Adding the media root to the urls

    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
        path("admin/", admin.site.urls),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


base.html : Create a templates folder at the root level and create a base.html file.

In the project urls.py

    urlpatterns = [
        path("admin/", admin.site.urls),
        path("", include("APPNAME.urls")),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

- Create a urls.py in the APPNAME

    from django.urls import path
    from . import views

    urlpatterns = [
        path("", views.VIEWNAME, name="VIEWNAME")
    ] 


### Acknowledgments

[Envatormarket](https://themeforest.net/category/template-kits/elementor)
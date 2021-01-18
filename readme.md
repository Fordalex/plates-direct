## Plates Direct

Time: 2 hours.

1. Creating a virtual environment

   python3 -m venv .venv

2. Activate the environment

   source .venv/bin/activate

3. Install django

   pip3 install django

4. Start a new project

   django-admin startproject PROJECTNAME .

5. Start a new app

   django-admin startapp APPNAME

6. Install new app (settings.py)

   INSTALLED_APPS = [
        "django.contrib.staticfiles",
        "APPNAME"
    ]

7. Import (settings.py)

    import os
    from os import path

8. Create path to tamplates

   "DIRS": [
            os.path.join(BASE_DIR, "templates")
    ],

9. Create path to static and media files

    STATIC_URL = "/static/"
    STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")

10. Adding the media root to the urls

    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
        path("admin/", admin.site.urls),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


11. base.html : Create a templates folder at the root level and create a base.html file.

12. In the project urls.py

    urlpatterns = [
        path("admin/", admin.site.urls),
        path("", include("APPNAME.urls")),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

13. Create a urls.py in the APPNAME

    from django.urls import path
    from . import views

    urlpatterns = [
        path("", views.VIEWNAME, name="VIEWNAME")
    ] 


#### Acknowledgments

[Envatormarket](https://themeforest.net/category/template-kits/elementor)
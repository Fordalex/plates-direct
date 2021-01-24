# Plates Direct

### Time

2Hours 30Mins # 17/01/2021 # 10:00pm - 12:30pm
    Set up the project.

1Hours 33Mins # 18/01/2021 # 20:40pm - 21:14pm / 13:26pm - 12:25pm
    Started on the home page, content and layout.

3Hours 18Mins # 20/01/2021 # 09:09am - 10:40am / 11:00am - 11:50am / 14:30pm - 15:27pm
    Added the registration input and style. 

51Mins # 22/01/2021 # 13:56pm - 14: 47pm
    Set up the context file for the shopping bag.

1Hour 20Mins # 22/01/2021 # 15:00pm - 16:20pm
    Added the options for the customer to only purchase/view one or muliple plates and the logic for the user to add items to the basket.

40Mins # 22/01/2021 # 16:50pm - 17:30pm
    Appended the items for the basket into the shopping page, started to style the items and added the total cost.

15 Mins # 22/01/2021
    Added more styling to the bag page.

1Hour 34Mins # 22/01/2021 # 21:05 - 22:39
    Added the logic so the user can empty the basket and remove individual items.

24/01/2021 # 07:00am - 



Time: 7Hours 21Mins.

### Feature left to implement

- When the user has pressed 'checkout' a promt will appear asking them if they want to add a kitting kit to their basket.

## Django project setup

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

Create a urls.py in the APPNAME

    from django.urls import path
    from . import views

    urlpatterns = [
        path("", views.VIEWNAME, name="VIEWNAME")
    ] 

## The Shopping Bag

Create a new app call 'bag'

    django-admin startapp bag

Added the app to the installed apps inside the settings.py file.

After the new app has been created, then create a new file inside the bag app called 'context.py'

    from decimal import Decimal
    from django.conf import settings

    def bag_contents(request):

        bag_items = []
        total = 0
        product_count = 0

        if total < settings.FREE_DELIVERY_THERESHOLD:
            delivery = total + STANDARD_DELIVERY
            free_delivery_delta = settings.FREE_DELIVERY_THERESHOLD - total
        else:
            delivery = 0
            free_delivery_delta = 0

        grand_total = delivery + total

        context = {
            'bag_items': bag_items,
            'total': total,
            'product_count': product_count,
            'delivery': delivery,
            'free_delivery_delta': free_delivery_delta,
            'free_delivery_threshold': settings.FREE_DELIVERY_THERESHOLD,
            'grand_total': grand_total,
        }

        return context

This is created so that is dictionary will be available for every page inside the project.

In the settings file add to the 'context_processors': 

    'bag.contexts.bag_contents',

Also, add the variables FREE_DELIVERY_THERESHOLD & STANDARD_DELIVERY in the settings.py file.

This dictionary can now be viewed on every page on the project. Access the value of the total with this syntax:

    {{ total }}

### Acknowledgments

[Envatormarket](https://themeforest.net/category/template-kits/elementor)
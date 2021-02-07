# Plates Direct

### Feature left to implement

- edit buttons on the checkout form.

- The customers amount isn't adding up correctly!

- When the user has pressed 'checkout' a promt will appear asking them if they want to add a kitting kit to their basket.

- Add content for the FAQs page.

- Add the payment logic and page.

- Add page for user to add documents on checkout.

- Need to add the logic for the increment values in the basket.

- When just a fitting kit is added, the toast mentions a uk number plate. "Added none...".

- Set the project up with Google analytics

- 404 error messages.

- JS on the form to make sure users can't go to checkout with an incorrect number plate.

- The menu needs to close then the user clicks off the menu.

- Allow the user to edit thier personal information and basket items, on the review order page, just redirect the user back to the relivant page.

- After order complete add the order to the database.

- GDPR tickbox for the customer.

- File document need to be handled somehow.

- when an item is removed from the toast on the replacement plates page, the page isn't redirect back to the correct page.

- Card details need to be checked with the customer address?

- After payment was made, refreshed the page and the payment was taken again??

- Show the user their order number on their order confirmation page.

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

IMPORTANT - if using sessions you need to connect the site up the the database, instrutions furture below.

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

### Hosting

Start off creating a Procfile with the following content:

    web: gunicorn plates_direct.wsgi:application

Install Gunicorn with the following commmand:

    pip install gunicorn

Go into the heroku 'settings', 'reveal config vars' and add the following variable:

    DISABLE_COLLECTSTATIC 1

Add the link to the allowed hosting in the project settings.

    ALLOWED_HOSTS = ['plates-direct.herokuapp.com']

Install whitenoise

    pip install whitenoise

Added this to the meddleware classes

    MIDDLEWARE_CLASSES = ( 'whitenoise.middleware.WhiteNoiseMiddleware',)

Then create the requirements.txt file

    pip freeze --local > requirements.txt

### Setting up the database

Create an env.py file

    import os
    os.environ.setdefault('DATABASE_URL', 'postgres://')

Install the following:

    pip3 install dj_database_url

Add to the settings:

    from os import path
    import dj_database_url
    if path.exists('env.py'):
        import env

In the settings.py file chagned the database setting to:

    if "DATABASE_URL" in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        print("postgres URL not found, using sqlite instead")
        DATABASES = {
            'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }

Then make the migrations:

    python3 manage.py migrate

### Stripe

Go to the stripe website, login and get the API keys.

Add <script src="https://js.stripe.com/v3/"></script> into the head of the base.html file.

[Intergration Builder](https://stripe.com/docs/payments/integration-builder)

Add the following to ta postload js block in the footer of your payment html page.

    {{ block.super }}
    {{ stripe_public_key|json_script:"id_stripe_public_key" }}
    {{ client_secret|json_script:"id_client_secret" }}
    <script src="{% static 'checkout/js/stripe_elements.js' %}"></script>

Add checkout folder in the static folder.

Add a css and js folder to the new checkout folder.

Then add a checkout.css file to the css folder.

Then add a stripe_elements.js file to new js folder.

Add the following to the stripe_elements.js file:

    var stripe_public_key = $('#id_stripe_public_key').text().slice(1,-1);
    var client_secret = $('#id_client_secret').text().slice(1,-1);
    var stripe = Stripe(stripe_public_key)
    var elements = stripe.elements();
    var card = elements.create('card');

Add the following to the settings.py file:

    STRIPE_CURRENCY = 'GBP'
    STRIPE_PUBLIC_KEY = os.environ.get('api_key')
    STRIPE_SECRET_KEY = os.environ.get('secret_key')

## Django fileField



## Django useful commands

Run project
    
    python manage.py runserver

Migrations

    python3 manage.py makemigrations

Migrations test

    python3 manage.py makemigrations --dry-run

Show migrations

    python3 manage.py showmigrations

Migrate

    python3 manage.py migrate

Migrate test

    python3 manage.py migrate --plan

Create super user

    python3 manage.py createsuperuser

Shell

    python3 manage.py shell

Delete all data

    python3 manage.py flush

Migrations set to zero

    python3 migrate APPNAME zero

Fake migrations

    python3 manage.py migrate --fake

Install coverage

    pip3 install coverage

Test using coverage

    coverage run --source=APPNAME manage.py test

Coverage html

    coverage html

Coverage report

    coverage report

Run server

    python3 -m http.server

### Acknowledgments

[Envatormarket](https://themeforest.net/category/template-kits/elementor)
# Couscous
Django application to manage (CRUD) debtors, their bank account data (IBAN) and invoices

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have [docker-machine](https://docs.docker.com/machine/install-machine/), [docker-compose](https://docs.docker.com/compose/install/) and [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed.

### Installing

Clone this repo

```
git clone https://github.com/jimmykamau/couscous.git
```

Create an app on the [Google Developer Console](https://developers.google.com/adwords/api/docs/guides/authentication) and grab the generated `client ID` and `client secret`.

Move into the `couscous` directory. Rename the `backend/couscous.env.exmaple` file to `backend/couscous.env` and update it with your credentials.

Build the containers

```
docker-compose build
```

Start the `db` service

```
docker-compose up -d db
```

Grab a `psql` shell from the `db` service
```
docker-compose exec db psql -U postgres -h db -p 5432
```

Create a database with the name you specified in the `couscous.env` file
```
CREATE DATABASE django_api;
```
Exit the shell
```
\q
```
Start the remaining services
```
docker-compose up
```
Visit the [localhost:8000/api/v1/](http://localhost:8000/api/v1/) URL to ensure everything is running properly.

Create a Django superuser
```
docker-compose exec backend ./manage.py createsuperuser
```

Log into the [admin](http://localhost:8000/admin/) site with the superuser credentials you just created. On the admin site go to the [Django OAuth Toolkit › Applications](http://localhost:8000/admin/oauth2_provider/application/) page and follow [these](https://github.com/RealmTeam/django-rest-framework-social-oauth2#setting-up-application) instructions to create a new app.

On another browser, visit the [admin](http://localhost:8000/admin/) page and sign in with your Google account.
Return to the browser signed in with your superuser account and give the new Google user permissions to all `debtor` and `invoice` fields, on the [edit user page](http://localhost:8000/admin/auth/user/<user-id>/change/). The permissions are under the `User permissions` tab.

Go back to the Google session and add some [debtors](http://localhost:8000/admin/debtor/debtor/) and [invoices](http://localhost:8000/admin/invoice/invoice/).

You can test the API by navigating to the [localhost:8000/api/v1/](http://localhost:8000/api/v1/) endpoint.

## Running the tests

You can run automated tests by executing the command below
```
docker-compose exec backend ./manage.py test
```
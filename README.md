![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome 

This is the Code Institute student PP4 readme for the project deployed to https://ib-driverblog-pp4.herokuapp.com/ 

------

## Release History

We continually tweak and adjust this.

Here is the version history:

**Jan 1 2023:** Begin MVP planning.
**Jan 23 2023:** Successful initial heroku deployment.

------

## Reminders

To install django, `pip3 install 'django<4' gunicorn`

and `pip3 install dj_database_url==0.5.0 psycopg2`
and `pip3 install dj3-cloudinary-storage`

To create the essential manage.py file and the key step in enabling the site to launch
use `django-admin startproject "put your appname here" .` don't forget the DOT at the end !!
We used driverblog for our blog about cars and other vehicles.
Don't forget the DOT at the end as this tells Django admin that we want to create our project in the current top level folder

Then use `python3 manage.py startapp vehicles` for example, to create the vehicles app within the driverblog project
And we update `settings.py` with details for the apps, hosts and secrets etc.

Use `python3 manage.py runserver` to launch web server

```
python3 manage.py runserver
```

We add the app with `python3 manage.py startapp blog` for example

Then we need to migrate the changes to the database etc with `python3 manage.py migrate`

Remember to update settings.py with all the env vars for secure access to Django and the Elephant DB in the database section

```
import os
import dj_database_url
if os.path.isfile('env.py'):
import env
```

To set up a app/database admin we need `python3 manage.py createsuperuser`

To install the app in Heroku you need:

1) Environment variables from env.py in your Heroku app settings
2) A Procfile to run the webserver i.e. `web: gunicorn driverblog.wsgi` 
    
    in this case to run the driverblog app on the gunicorn wsgi webserver.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.


**Anything more?**

Yes! We'd strongly encourage you to look at the source code!

---

Happy coding!

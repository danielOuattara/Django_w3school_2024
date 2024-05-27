# Django Create App

## What is an App?

A `Django app` is a `web application` that has a specific
meaning in the project, like a home page, a contact form,
or a members database.

In this tutorial we will create an app that allows to list
and register members in a database.

But first, let's just create a simple Django app that displays
`Hello World!`.

## Create App

**I will name my app members.**

Start by navigating to the selected location where you want to
store the app, in my case the `my_tennis_club` folder, and run
the command below.

If the server is still running, and you are not able to write
commands, press [CTRL] [BREAK], or [CTRL] [C] to stop the server
and you should be back in the virtual environment.

```bash
python3 manage.py startapp members
```

Django creates a folder named members in my project, with this
content:

```bash
my_tennis_club
    manage.py
    my_tennis_club/
    members/
        migrations/
            **init**.py
        **init**.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py

```

These are all files and folders with a specific meaning.
You will learn about most of them later in this tutorial.

First, take a look at the file called `views.py`.

This is where we gather the information we need to send back
a proper response.

You will learn more about views in the next chapter.

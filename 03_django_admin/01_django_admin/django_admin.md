# Django Admin

##  Django Admin

`Django Admin` is a really great tool in Django.
It is actually a CRUD user interface of all your models!

It is free and comes ready-to-use with Django:

![image](https://www.w3schools.com/django/screenshot_django_admin_login6.png)

##  Getting Started

To enter the admin user interface, start the server by
navigating to the `/my_tennis_club` folder and execute
this command:

```bash
py manage.py runserver
```

In the browser window, navigate `http://127.0.0.1:8000/admin/` in the address bar.

The result should look like this:

![image](https://www.w3schools.com/django/screenshot_django_admin_login.png)

The reason why this URL goes to the Django admin log in page
can be found in the `/my_tennis_club/urls.py` file of your project:

```py
# my_tennis_club/my_tennis_club/urls.py:

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('members.urls')),
    path('admin/', admin.site.urls),
]
```

The `urlpatterns[]` list takes requests going to `admin/`
and sends them to `admin.site.urls`, which is part of a
the built-in application that comes with Django, which
contains a lot of functionality and user interfaces, one
of them being the log-in user interface.

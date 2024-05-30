# Django URLS

##  URLs

Create a file named `my_tennis_club/members/urls.py`
and add this code there:

```py
# my_tennis_club/members/urls.py:

from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
]
```

The `urls.py` file you just created is specific for the members
application.

We have to do some routing in the root directory
`/my_tennis_club/my_tennis_club` as well.

This may seem complicated, but for now, just follow the instructions below.

There is a file called `urls.py` on the `my_tennis_club` folder,
open that file and add the `include` module in the `import`
statement, and also add a `path()` function in the `urlpatterns[]`
list, with arguments that will route users that comes in via 127.0.0.1:8000/.

```py
# my_tennis_club/my_tennis_club/urls.py:

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('members.urls')),
    path('admin/', admin.site.urls),
]

```

If the server is not running, navigate to the
`/my_tennis_club folder` and execute this command in the
command prompt:

```sh
python3 manage.py runserver
```

In the browser window, navigate to  127.0.0.1:8000/members/
in the address bar.

![image](https://www.w3schools.com/django/screenshot_django_hello_world.png)

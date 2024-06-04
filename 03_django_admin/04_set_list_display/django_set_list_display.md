# Django Admin - Set Fields to Display

##  Make the List Display More Reader-Friendly

When you display a Model as a list, Django displays each
record as the string representation of the record object,
which in our case is `Member object (1)`, `Member object(2)` etc.:

![image](https://www.w3schools.com/django/screenshot_django_admin3.png)

To change this to a more reader-friendly format, we have
two choices:

1. Change the string representation function, `__str__()`
   of the Member Model
2. Set the `list_details` property of the Member Model

##  Change the String Representation Function

To change the string representation, we have to define
the `__str__()` function of the Member Model in `members/models.py`,
like this:

```py
# my_tennis_club/members/models.py:

from django.db import models

class Member(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)

  def __str__(self):
    return f"{self.first_name} {self.last_name}"

```

which gives us this result:

![image](https://www.w3schools.com/django/screenshot_django_admin4.png)

```text
NOTE:
-----

Defining our own `__str__()` function is not a Django feature, 
it is how to change the string representation of objects in Python. 

Read more about Python objects in our Python object tutorial at (https://www.w3schools.com/python_classes.asp).

```

##  Set list_display

We can control the fields to display by specifying them
in in a `list_display` property in the `/members/admin.py`
file.

- First create a `MemberAdmin() class` and specify the `list_display`
  tuple, like this:

```py
# my_tennis_club/members/admin.py:

from django.contrib import admin
from .models import Member

# Register your models here

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)
  
admin.site.register(Member, MemberAdmin)
```

```text
NOTE:
-----
Remember to add the `MemberAdmin` as an argument in 
the `admin.site.register(Member, MemberAdmin)`.
```

Now go back to the browser and you should get this result:

# Django QuerySet - Get Data

##  Get Data

There are different methods to get data from a model
into a QuerySet.

## The values() Method

The `values()` method allows you to return each object
as a Python dictionary, with the names and values as
key/value pairs:

```py
# members/views.py:

from django.http import HttpResponse
from django.template import loader
from .models import Member

def testing(request):
  members = Member.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'members': members,
  }
  return HttpResponse(template.render(context, request))
```

## Return Specific Columns

The `values_list()` method allows you to return only the
columns that you specify.

> Return only the first_name columns:

```py
# members/views.py:

from django.http import HttpResponse
from django.template import loader
from .models import Member

def testing(request):
  first_name_list = Member.objects.values_list('first_name')
  template = loader.get_template('template.html')
  context = {
    'first_name_list': first_name_list,
  }
  return HttpResponse(template.render(context, request))
```

##  Return Specific Rows

You can filter the search to only return specific rows/records,
by using the `filter()` method.

> Return only the records where first_name is 'Emil'

```py
# members/views.py:

from django.http import HttpResponse
from django.template import loader
from .models import Member

def testing(request):
  emil = Member.objects.filter(first_name='Emil').values()
  template = loader.get_template('template.html')
  context = {
    'emil': emil,
  }
  return HttpResponse(template.render(context, request))
```

You will learn more about the filter() method in the next chapter.

#  Django Template Variables

##  Template Variables

In Django templates, you can render variables by putting
them inside `{{ }}` brackets:

```html
<!-- /members/templates/template.html: -->

<h1>Hello {{ first_name }}, how are you?</h1>

```

##  Create Variable in View

The variable `first_name` in the example above was sent to the
template via a view:

```py
# /my_tennis_club/members/views.py

from django.http import HttpResponse
from django.template import loader

# ...

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'first_name': 'Linus',
  }
  return HttpResponse(template.render(context, request))
```

As you can see in the view above, we create an object named context
and fill it with data, and send it as the first parameter in the
`template.render()` function.

## Create Variables in Template

You can also create variables directly in the template, by using
the `{% with %}` template tag.

The variable is available until the `{% endwith %}` tag appears:

```html

<!-- /members/templates/template.html: -->

{% with first_name="Tobias" %}
    <h1>Hello {{ first_name }}, how are you?</h1>
{% endwith %}
```

You will learn more about template tags in the next chapter.

##  Data From a Model

The example above showed a easy approach on how to create and
use variables in a template.

Normally, most of the external data you want to use in a template,
comes from a model.

We have created a model in the previous chapters, called `Member`,
which we will use in many examples in the next chapters of this
tutorial.

To get data from the `Member` model, we will have to import it in
the `views.py` file, and extract data from it in the view:

```py

# members/views.py:

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member

def testing(request):
  my_members = Member.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'my_members': my_members,
  }
  return HttpResponse(template.render(context, request))
```

Now we can use the data in the template:

```html
<!-- /members/templates/template.html: -->

<ul>
  {% for x in my_members %}
    <li>{{ x.first_name }}</li>
  {% endfor %}
</ul>
```

We use the Django template tag `{% for %}` to loop through the
members.

You will learn more about template tags in the next chapter.

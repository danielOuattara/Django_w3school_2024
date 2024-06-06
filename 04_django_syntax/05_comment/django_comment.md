# Django comment Tag

## Comments

Comments allows you to have sections of code that should be ignored.

```html
<h1>Welcome Everyone</h1>
{% comment %}
  <h1>Welcome ladies and gentlemen</h1>
{% endcomment %}
```

##  Comment Description

You can add a message to your comment, to help you remember why you
wrote the comment, or as message to other people reading the code.

> Add a description to your comment:

```html
<h1>Welcome Everyone</h1>
{% comment "this was the original welcome message" %}
    <h1>Welcome ladies and gentlemen</h1>
{% endcomment %}
```

##  Smaller Comments

You can also use the `{# ... #}` tags when commenting out code,
which can be easier for smaller comments:Example

> Comment out the word Everyone:

```html
<h1>Welcome{# Everyone#}</h1>
```

##  Comment in Views

Views are written in Python, and Python comments are written with
the `#` character:

> Comment out a section in the view:

```py
from django.http import HttpResponse
from django.template import loader

def testing(request):
  template = loader.get_template('template.html')
  #context = {

# 'var1': 'John'

  #}
  return HttpResponse(template.render())

```

> Read more about Python Comments in out [Python Comment Tutorial](https://www.w3schools.com/python/python_comments.asp).

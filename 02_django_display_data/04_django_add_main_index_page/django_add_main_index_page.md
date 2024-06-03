# Django Add Main Index Page

##  Main Index Page

Our project needs a main page.

The main page will be the landing page when someone visits
the root folder of the project.

Now, you get an error when visiting the root folder of your
project:

(<http://127.0.0.1:8000/>)

Start by creating a template called `main.html`

### Main

```html
<!-- my_tennis_club/members/templates/main.html: -->

{% extends "master.html" %}

{% block title %}
  My Tennis Club
{% endblock %}

{% block content %}
  <h1>My Tennis Club</h1>

  <h3>Members</h3>
  
  <p>Check out all our <a href="members/">members</a></p>
  
{% endblock %}
```

##  Create new View

Then create a new view called `main`, that will deal with
incoming requests to root of the project:

```py
# my_tennis_club/members/views.py:

from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  my_members = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'my_members': my_members,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  my_member = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'my_member': my_member,
  }
  return HttpResponse(template.render(context, request))
  
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

```

The main view does the following:

- loads the `main.html` template.
- Outputs the HTML that is rendered by the template.

## Add URL

Now we need to make sure that the root url points to the correct view.

Open the `urls.py` file and add the `main` view to the `urlpatterns` list:

```py
# my_tennis_club/members/urls.py:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
]
```

##  Add Link Back to Main

The members page is missing a link back to the main page, so let's
add that in the `all_members.html` template, in the content block:

```html
<!-- my_tennis_club/members/templates/all_members.html: -->

{% extends "master.html" %}

{% block title %}
  My Tennis Club - List of all members
{% endblock %}

{% block content %}

  <p><a href="/">HOME</a></p>

  <h1>Members</h1>
  
  <ul>
    {% for x in my_members %}
      <li><a href="details/{{ x.id }}">{{ x.first_name }} {{ x.last_name }}</a></li>
    {% endfor %}
  </ul>
{% endblock %}
```

If you have followed all the steps on your own computer, you can see
the result in your own browser: (<http://127.0.0.1:8000/>)

If the server is down, you have to start it again with the runserver
command:

```bash
py manage.py runserver
```

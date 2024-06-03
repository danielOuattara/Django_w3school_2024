# Django Add Master Template

## The extends Tag

In the previous pages we created two templates:

- one for listing all members
- one for details about a member.

These templates have a set of HTML code that are the same
for both templates.

Django provides a way of making a `parent template` that you
can include in all pages to do the stuff that is the same in
all pages.

Start by creating a template called `master.html`, with all
the necessary HTML elements:

```html
<!-- my_tennis_club/members/templates/master.html: -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{% block title %}{% endblock %}</title>
</head>
<body>

{% block content %}
{% endblock %}

</body>
</html>
```

Can you see `Django block Tag` inside the `<title>` element,
and also inside the `<body>` element?

Theses are placeholders: telling Django to replace this block
with content from other sources.

##  Modify Templates

Now the two templates,`all_members.html` and `details.html` can
use this `master.html` template.

This is done by including the master template with the `{% extends %} tag`,
and inserting a `title block` and a `content block`:

###  Members

```html
<!-- my_tennis_club/members/templates/all_members.html: -->

{% extends "master.html" %}

{% block title %}
  My Tennis Club - List of all members
{% endblock %}

{% block content %}
  <h1>Members</h1>
  
  <ul>
    {% for x in my_members %}
      <li><a href="details/{{ x.id }}">{{ x.first_name }} {{ x.last_name }}</a></li>
    {% endfor %}
  </ul>
{% endblock %}
```

###  Details

```html
<!-- my_tennis_club/members/templates/details.html: -->

{% extends "master.html" %}

{% block title %}
  Details about {{ my_member.first_name }} {{ my_member.last_name }}
{% endblock %}

{% block content %}
  <h1>{{ my_member.first_name }} {{ my_member.last_name }}</h1>
  
  <p>Phone {{ my_member.phone }}</p>
  <p>Member since: {{ my_member.joined_date }}</p>
  
  <p>Back to <a href="/members">Members</a></p>
  
{% endblock %}
```

If you have followed all the steps on your own computer,
you can see the result in your own browser: (<http://127.0.0.1:8000/members/>)

If the server is down, you have to start it again with the runserver
command:

```py
python3 manage.py runserver 
```

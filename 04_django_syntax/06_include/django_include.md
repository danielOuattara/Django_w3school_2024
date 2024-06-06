#  Django include Tag

##  Include

The `include` tag allows you to include a template inside
the current template.

This is useful when you have a block of content that is the
same for many pages.

```html
<!-- templates/footer.html: -->
<p>You have reached the bottom of this page, thank you for your time.</p>
```

```html
<!-- templates/template.html: -->
<h1>Hello</h1>

<p>This page contains a footer in a template.</p>

{% include 'footer.html' %}
```

##  Variables in Include

You can send variables into the template by using the `with` keyword.

In the include file, you refer to the variables by using the
{{ variablename }} syntax:

```html
<!-- templates/mymenu.html: -->

<div>HOME | {{ me }} | ABOUT | FORUM | {{ sponsor }}</div>
```

```html
<!-- templates/template.html: -->

<!DOCTYPE html>
<html>
<body>

{% include "mymenu.html" with me="TOBIAS" sponsor="W3SCHOOLS" %}

<h1>Welcome</h1>

<p>This is my webpage</p>

</body>
</html>
```

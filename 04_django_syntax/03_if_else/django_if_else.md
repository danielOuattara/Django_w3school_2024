# Django if Tag

##  If Statement

An `if` statement evaluates a variable and executes a block of code
if the value is true.

```html
{% if greeting == 1 %}
  <h1>Hello 1</h1>
{% endif %}
```

##  Elif

The `elif` keyword says `if the previous conditions were not true, then try this condition`.

```html
{% if greeting == 1 %}
  <h1>Hello &</h1>
{% elif greeting == 2 %}
  <h1>Welcome 2</h1>
{% endif %}
```

##  Else

The `else` keyword catches anything which isn't caught by
the preceding conditions.

```html
{% if greeting == 1 %}
  <h1>Hello</h1>
{% elif greeting == 2 %}
  <h1>Welcome</h1>
{% else %}
  <h1>Goodbye</h1>
{% endif %}

```

##  Operators

The above examples uses the `==` operator, which is used
to check if a variable is equal to a value, but there are
many other operators you can use, or you can even drop
the operator if you just want to check if a variable is not
empty:

```html
<!-- check not empty only -->
{% if greeting %}
  <h1>Hello</h1>
{% endif %}
```

## ==  Is equal to

```html
{% if greeting == 2 %}
  <h1>Hello</h1>
{% endif %}
```

##  !=  Is not equal to

```html
{% if greeting != 1 %}
  <h1>Hello</h1>
{% endif %}
```

##  <  Is less than

```html
{% if greeting < 3 %}
  <h1>Hello</h1>
{% endif %}
```

##  <= Is less than, or equal to

```html
{% if greeting <= 3 %}
  <h1>Hello</h1>
{% endif %}
```

##   > Is greater than

```html
{% if greeting > 1 %}
  <h1>Hello</h1>
{% endif %}
```

##  >= Is greater than, or equal to

```html

{% if greeting >= 1 %}
  <h1>Hello</h1>
{% endif %}

```

##  and

To check if more than one condition is true.

```html

{% if greeting == 1 and day == "Friday" %}
  <h1>Hello Weekend!</h1>
{% endif %}
```

##  or

To check if one of the conditions is true.

```html
{% if greeting == 1 or greeting == 5 %}
  <h1>Hello</h1>
{% endif %}
```

##  and/or

Combine and and or.

```html
{% if greeting == 1 and day == "Friday" or greeting == 5 %}
```

```text
NOTE:
------

Parentheses are not allowed in if statements in Django, 
so when you combine `and` and `or` operators, it is 
important to know that parentheses are added around `and` 
but not around or.
```

Meaning that the above example is read by the interpreter like this:

{% if (greeting == 1 and day == "Friday") or greeting == 5 %}

##  in

To check if a certain item is present in an object.

```html
{% if 'Banana' in fruits %}
  <h1>Hello</h1>
{% else %}
  <h1>Goodbye</h1>
{% endif %}
```

##  not in

To check if a certain item is not present in an object.

```html
{% if 'Banana' not in fruits %}
  <h1>Hello</h1>
{% else %}
  <h1>Goodbye</h1>
{% endif %}
```

##  is

Check if two objects are the same.

This operator is different from the `==` operator,
because the `==` operator checks the values of two objects,
but the is operator checks the identity of two objects.

In the view we have two objects, x and y, with the same values:

```py
# views.py

from django.http import HttpResponse
from django.template import loader

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'x': ['Apple', 'Banana', 'Cherry'],
    'y': ['Apple', 'Banana', 'Cherry'],
  }
  return HttpResponse(template.render(context, request))  

```

The two objects have the same value, but is it the same object?

```html

{% if x is y %}
  <h1>YES</h1>
{% else %}
  <h1>NO</h1>
{% endif %}
```

Let us try the same example with the == operator instead:

```html
{% if x == y %}
  <h1>YES</h1>
{% else %}
  <h1>NO</h1>
{% endif %}
```

How can two objects be the same?

Well, if you have two objects that points to the same object,
then the `is` operator evaluates to true:

We will demonstrate this by using the {% with %} tag, which
allows us to create variables in the template:

```html
{% with var1=x var2=x %}
  {% if var1 is var2 %}
    <h1>YES</h1>
  {% else %}
    <h1>NO</h1>
  {% endif %}
{% endwith %}
```

##  is not

To check if two objects are not the same.

```html
{% if x is not y %}
  <h1>YES</h1>
{% else %}
  <h1>NO</h1>
{% endif %}
```

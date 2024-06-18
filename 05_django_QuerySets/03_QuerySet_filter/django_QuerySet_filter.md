# Django QuerySet - Filter

## QuerySet Filter

The `filter()` method is used to filter your search,
and allows you to return only the rows that matches
the search term.

As we learned in the previous chapter, we can filter
on field names like this:

> Return only the records where the first_name is 'Emil':

```py
emil = Member.objects.filter(first_name='Emil').values()
```

In SQL, the above statement would be written like this:

```sql
SELECT * 
FROM members 
WHERE first_name = 'Emil';
```

##  AND

The `filter()` method takes the arguments as **kwargs (keyword arguments),
so you can filter on more than one field by separating
them by a comma.

> Return records where last_name is "Refsnes" `AND` id is 2:

```py
refsnes = Member.objects.filter(last_name='Refsnes', id=2).values()
```

In SQL, the above statement would be written like this:

```sql
SELECT * 
FROM members 
WHERE last_name = 'Refsnes' AND id = 2;
```

## OR

To return records where `first_name` is Emil `AND` `first_name`
is Tobias; meaning: returning records that matches either query,
not necessarily both, is not as easy as the `AND` example above.

- We can use `multiple filter()` methods, separated by a pipe `|`
  character. The results will merge into one model.

> Return records where first_name is either "Emil" or Tobias":

```py
my_data = Member.objects.filter(first_name='Emil').values() | Member.objects.filter(first_name='Tobias').values()
```

- Another common method is to import and use `Q` expressions:

> Return records where first_name is either "Emil" or Tobias":

```py
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q

def testing(request):
  my_data = Member.objects.filter(Q(first_name='Emil') | Q(first_name='Tobias')).values()
  template = loader.get_template('template.html')
  context = {
    'my_data': my_data,
  }
  return HttpResponse(template.render(context, request))
```

In SQL, the above statement would be written like this:

```sql
SELECT * 
FROM members 
WHERE first_name = 'Emil' OR first_name = 'Tobias';
```

## Field Lookups

Django has its own way of specifying SQL statements and WHERE clauses.

To make specific where clauses in Django, use `Field lookups`.

Field lookups are keywords that represents specific SQL keywords.

### Use the __startswith keyword

```py
.filter(first_name__startswith='L');
```

Is the same as the SQL statement:

```sql
WHERE first_name LIKE 'L%'
```

The above statement will return records where first_name starts with 'L'.

## Field Lookups Syntax

All Field lookup keywords must be specified with the fieldname, followed
by two (2) underscore characters, and the keyword.

In our `Member` model, the statement would be written like this:

> Return the records where first_name starts with the letter 'L':

```py
my_data = Member.objects.filter(first_name__startswith='L').values()
```

Field Lookups Reference

A list of all field look up keywords:
|    Keyword   |                    Description                   |
|:------------:|:------------------------------------------------:|
| contains     | Contains the phrase                              |
| icontains    | Same as contains, but case-insensitive           |
| date         | Matches a date                                   |
| day          | Matches a date (day of month, 1-31) (for dates)  |
| endswith     | Ends with                                        |
| iendswith    | Same as endswidth, but case-insensitive          |
| exact        | An exact match                                   |
| iexact       | Same as exact, but case-insensitive              |
| in           | Matches one of the values                        |
| isnull       | Matches NULL values                              |
| gt           | Greater than                                     |
| gte          | Greater than, or equal to                        |
| hour         | Matches an hour (for datetimes)                  |
| lt           | Less than                                        |
| lte          | Less than, or equal to                           |
| minute       | Matches a minute (for datetimes)                 |
| month        | Matches a month (for dates)                      |
| quarter      | Matches a quarter of the year (1-4) (for dates)  |
| range        | Match between                                    |
| regex        | Matches a regular expression                     |
| iregex       | Same as regex, but case-insensitive              |
| second       | Matches a second (for datetimes)                 |
| startswith   | Starts with                                      |
| istartswith  | Same as startswith, but case-insensitive         |
| time         | Matches a time (for datetimes)                   |
| week         | Matches a week number (1-53) (for dates)         |
| week_day     | Matches a day of week (1-7) 1 is sunday          |
| iso_week_day | Matches a ISO 8601 day of week (1-7) 1 is monday |
| year         | Matches a year (for dates)                       |
| iso_year     | Matches an ISO 8601 year (for dates)             |

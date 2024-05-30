# Django Insert Data

##  Add Records

The `Members` table created in the previous chapter is empty.

We will use the Python interpreter (Python shell) to add some
members to it.

To open a Python shell, type this command:

```bash
python3 manage.py shell
```

Now we are in the shell, the result should be something like this:

```py
Python 3.11.2 (main, Mar 13 2023, 12:18:29) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>
```

At the bottom, after the three >>> write the following:

```py
>>> from members.models import Member
```

Hit [enter] and write this to look at the empty Member table:

```py
>>> Member.objects.all()
```

This should give you an empty QuerySet object, like this:

```py
<QuerySet []>
```

A `QuerySet` is a collection of data from a database.

Read more about `QuerySets` in the [Django QuerySet](https://www.w3schools.com/django/django_queryset.php) chapter.

Add a record to the table, by executing these two lines:

```py
>>> member = Member(first_name='Emil', last_name='Refsnes')
>>> member.save()
```

Execute this command to see if the Member table got a member:

```py
>>> Member.objects.all().values()
```

Hopefully, the result will look like this:

```py
<QuerySet [{'id': 1, 'first_name': 'Emil', 'last_name': 'Refsnes'}]>
```

## Add Multiple Records

You can add multiple records by making a list of Member objects,
and execute .save() on each entry:

```py
>>> member1 = Member(first_name='Tobias', last_name='Refsnes')
>>> member2 = Member(first_name='Linus', last_name='Refsnes')
>>> member3 = Member(first_name='Lene', last_name='Refsnes')
>>> member4 = Member(first_name='Stale', last_name='Refsnes')
>>> member5 = Member(first_name='Jane', last_name='Doe')
>>> members_list = [member1, member2, member3, member4, member5]
>>> for x in members_list:
>>> x.save()
>>> 
>>> 

```

Now there are 6 members in the Member table:

```py
>>> Member.objects.all().values()
<QuerySet [{'id': 1, 'first_name': 'Emil', 'last_name': 'Refsnes'},
{'id': 2, 'first_name': 'Tobias', 'last_name': 'Refsnes'},
{'id': 3, 'first_name': 'Linus', 'last_name': 'Refsnes'},
{'id': 4, 'first_name': 'Lene', 'last_name': 'Refsnes'},
{'id': 5, 'first_name': 'Stale', 'last_name': 'Refsnes'},
{'id': 6, 'first_name': 'Jane', 'last_name': 'Doe'}]>
```

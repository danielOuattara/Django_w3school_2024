# Django Update Data

##  Update Records

To update records that are already in the database, we first
have to get the record we want to update:

```py
>>> from members.models import Member
>>> x = Member.objects.all()[4]
```

`x` will now represent the member at `index 4`, which is
`Stale Refsnes`, but to make sure, let us see if that is
correct:

```py
>>> x.first_name
```

This should give you this result:

```py
'Stale'
```

Now we can change the values of this record:

```py
>>> x.first_name = "Stalikken"
>>> x.save()
>>>
```

Execute this command to see if the Member table got updated:

```py
>>> Member.objects.all().values()
```

Hopefully, the result will look like this:

```py
<QuerySet [{'id': 1, 'first_name': 'Emil', 'last_name': 'Refsnes'},
{'id': 2, 'first_name': 'Tobias', 'last_name': 'Refsnes'},
{'id': 3, 'first_name': 'Linus', 'last_name': 'Refsnes'},
{'id': 4, 'first_name': 'Lene', 'last_name': 'Refsnes'},
{'id': 5, 'first_name': 'Stalikken', 'last_name': 'Refsnes'}, # <--- this one
{'id': 6, 'first_name': 'Jane', 'last_name': 'Doe'}]>
```

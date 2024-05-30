# Django Delete Data

##  Delete Records

To delete a record in a table, start by getting the record
you want to delete:

```py
>>> from members.models import Member
>>> x = Member.objects.all()[5]
```

x will now represent the member at index 5, which is "Jane Doe",
 but to make sure, let us see if that is correct:

```py
>>> x.first_name
```

This should give you this result:

```py
'Jane'
```

Now we can delete the record:

```py
>>> x.delete()
```

The result will be:

```py
(1, {'members.Member': 1})
```

Which tells us how many items were deleted, and from
which Model.

If we look at the Member Model, we can see that
'Jane Doe' is removed from the Model:

```py
>>> Member.objects.all().values()
<QuerySet [{'id': 1, 'first_name': 'Emil', 'last_name': 'Refsnes'},
{'id': 2, 'first_name': 'Tobias', 'last_name': 'Refsnes'},
{'id': 3, 'first_name': 'Linus', 'last_name': 'Refsnes'},
{'id': 4, 'first_name': 'Lene', 'last_name': 'Refsnes'},
{'id': 5, 'first_name': 'Stalikken', 'last_name': 'Refsnes'}]>
```

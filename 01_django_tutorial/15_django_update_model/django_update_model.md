# Django Update Model

## Add Fields in the Model

To add a field to a table after it is created,
open the `/members/models.py` file,
and make your changes:

```py
# my_tennis_club/members/models.py:

from django.db import models

class Member(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  phone = models.IntegerField()
  joined_date = models.DateField()
```

As you can see, we want to add `phone` and `joined_date`
to our Member Model.

This represent a change in the Model's structure, and
therefore we have to make a migration to tell Django
that it must update the database:

```bash
python3 manage.py makemigrations members
```

Which, in my case, will result in a prompt, because
I try to add fields that are not allowed to be null,
in a table that already contains records.

As you can see, Django asks if I want to provide the
fields with a specific value, or if I want to stop
the migration and fix it in the model:

```bash
py manage.py makemigrations members

It is impossible to add a non-nullable field 'joined_date' 
to member without specifying a default. This is because 
the database needs something to populate existing rows.

Please select a fix:
 1) Provide a one-off default now (will be set on all existing 
 rows with a null value for this column)
 2) Quit and manually define a default value in models.py.
Select an option:
```

I will select `option 2`, and open the `/members/models.py` file
again and allow NULL values for the two new fields:

```py
# my_tennis_club/members/models.py:

from django.db import models

class Member(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
```

And make the migration once again:

```py
py manage.py makemigrations members
```

Which will result in this:

```bash
python3 manage.py makemigrations members

Migrations for 'members':
  members/migrations/0002_member_joined_date_member_phone.py
    - Add field joined_date to member
    - Add field phone to member
```

Run the migrate command:

```bash
python3 manage.py migrate
```

Which will result in this output:

```bash
python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, members, sessions
Running migrations:
  Applying members.0002_member_joined_date_member_phone... OK

```

- After that check the migration through `python3 manage.py sqlmigrate members 0002`

```sql
 python3 manage.py sqlmigrate members 0002
BEGIN;
--
-- Add field joined_date to member
--
ALTER TABLE "members_member" ADD COLUMN "joined_date" date NULL;
--
-- Add field phone to member
--
ALTER TABLE "members_member" ADD COLUMN "phone" integer NULL;
COMMIT;
```

##  Insert Data

We can insert data to the two new fields with the same approach
as we did in the Update Data chapter:

- First we enter the Python Shell:

```bash
python3 manage.py shell
```

Now we are in the shell, the result should be something like this:

```bash
Python 3.11.2 (main, Mar 13 2023, 12:18:29) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>
```

At the bottom, after the three `>>>` write the following (and hit [enter] for each line):

```py
>>> from members.models import Member
>>> x = Member.objects.all()[0]
>>> x.phone = 5551234
>>> x.joined_date = '2022-01-05'
>>> x.save()
```

This will insert a phone number and a date in the Member Model,
at least for the first record, the four remaining records will
for now be left empty. We will deal with them later in the tutorial.

Execute this command to see if the Member table got updated:

```py
>>> Member.objects.all().values()
```

The result should look like this:

```py
<QuerySet [
{'id': 1, 'first_name': 'Emil', 'last_name': 'Refsnes', 'phone': 5551234, 'joined_date': datetime.date(2022, 1, 5)},
{'id': 2, 'first_name': 'Tobias', 'last_name': 'Refsnes', 'phone': None, 'joined_date': None},
{'id': 3, 'first_name': 'Linus', 'last_name': 'Refsnes', 'phone': None, 'joined_date': None},
{'id': 4, 'first_name': 'Lene', 'last_name': 'Refsnes', 'phone': None, 'joined_date': None},
{'id': 5, 'first_name': 'Stalikken', 'last_name': 'Refsnes', 'phone': None, 'joined_date': None}]>
```

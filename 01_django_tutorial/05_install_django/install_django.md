# Install Django

Now, that we have created a virtual environment, we are
ready to install Django.

**Note: Remember to install Django while the virtual environment is activated !**

Django is installed using `pip3`, with this command:

```bash
# Windows:
(env) C:\Users\Your Name>py -m pip3 install Django

# Unix/MacOS:
(env) ... $ python -m pip3 install Django
```

Which will give a result that looks like this (at least on my
Windows machine):

```bash
Collecting Django
  Downloading Django-4.0.3-py3-none-any.whl (8.0 MB)
      |████████████████████████████████| 8.0 MB 2.2 MB/s
Collecting sqlparse>=0.2.2
  Using cached sqlparse-0.4.2-py3-none-any.whl (42 kB)
Collecting asgiref<4,>=3.4.1
  Downloading asgiref-3.5.0-py3-none-any.whl (22 kB)
Collecting tzdata; sys_platform == "win32"
  Downloading tzdata-2021.5-py2.py3-none-any.whl (339 kB)
      |████████████████████████████████| 339 kB 6.4 MB/s
Installing collected packages: sqlparse, asgiref, tzdata, Django
Successfully installed Django-4.0.3 asgiref-3.5.0 sqlparse-0.4.2 tzdata-2021.5
WARNING: You are using pip version 20.2.3; however, version 22.3 is available.
You should consider upgrading via the 'C:\Users\Your Name\env\Scripts\python.exe -m pip install --upgrade pip' command.
```

That's it! Now you have installed Django in your new project,
running in a virtual environment!

##  Windows, Mac, or Unix?

You can run this project on either one. There are some small
differences, like when writing commands in the command prompt,
Windows uses `py` as the first word in the command line, while
Unix and MacOS use `python3`:

```bash
# Windows:
py --version

# Unix/MacOS:
python3 --version
```

**In the rest of this tutorial, we will be using the Linux/Debian command.**

## Check Django Version

You can check if Django is installed by asking for its version
number like this:

```bash
(env) django-admin --version
```

If Django is installed, you will get a result with the version number:
5.0.6

##  What's Next?

Now you are ready to create a Django project in a virtual environment
on your computer.

In the next chapters of this tutorial we will create a Django project
and look at the various features of Django and hopefully make you a
Django developer.

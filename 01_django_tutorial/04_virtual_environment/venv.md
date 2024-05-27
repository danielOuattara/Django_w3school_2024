# Django - Create Virtual Environment

## Virtual Environment

It is suggested to have a dedicated virtual environment for
each Django project, and one way to manage a virtual environ-
ment is `venv`, which is included in Python.

The name of the virtual environment is your choice, in this
tutorial we will call it `env`.

Type the following in the command prompt, remember to navigate
to where you want to create your project:

**Windows:**

```bash
py -m venv env
```

**Unix/MacOS:**

```bash
python -m venv env
```

This will set up a virtual environment, and create a folder named
`env` with subfolders and files, like this:

```bash
env
  Include
  Lib
  Scripts
  pyvenv.cfg
```

Then you have to activate the environment, by typing this command:

**Windows:**

```bash
env\Scripts\activate.bat
```

**Unix/MacOS:**

```bash
source env/bin/activate
```

Once the environment is activated, you will see this result in the
command prompt:

**Windows:**

```bash
(env) C:\Users\Your Name>
```

**Unix/MacOS:**

```bash
(env) ... $
```

**Note:** You must activate the virtual environment every time you
open the command prompt to work on your project.

##  Install Django

In the next chapter you will finally learn how to install Django.

# Django-Portfolio
Nice Portfolio with Python Django 2.0.2

### Step by Step - How to build your own portfolio with Django.

**Here some of the commands we will use for this project:**

**Creating virtual environment (Mac)**

``pip3 install virtualenv``

**Creating a new project**
   
```django-admin startproject projectname```

**Add an app to a project**

```python3 manage.py startapp appname```

**Starting the server**

``python3 manage.py runserver``

**Creating migrations**

``python3 manage.py makemigrations``

**Migrate the database**

``python3 manage.py migrate``

**Creating a Super User for the admin panel**

``python3 manage.py createsuperuser``

**Collecting static files into one folder**

``python3 manage.py collectstatic``

    
# The following instructions response to Mac OS

**Let's start our project**

Create a folder called ``Django-Project``

``cd Django-Project``

To install virtualenv type. 

``pip3 install virtualenv`` Here I am assuming you have pip3 installed.

Create a virtual environment

``virtualenv myenv``

Activate your virtual environment

`` source myenv/bin/activate ``

You should see something like this: ``(myenv) yourmachina:Django-Project yourusername$``

**Note** if you want to get out from your environment type: ``deactivate``

**Now let's create our Django project**

``django-admin startproject portfolio``

At this point you should see this tree:

```
portfolio/
├── manage.py
└── portfolio
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

If you see we have 2 folders called portfolio and this could cause confusion.

Let's rename the first folder as ``portfolio-project``

You can achieve this typing: ``mv portfolio/ portfolio-project``

Now you should have something like this:

```
portfolio-project/
  ├── manage.py
  └── portfolio
      ├── __init__.py
      ├── settings.py
      ├── urls.py
      └── wsgi.py
```

Is time to install Django

``pip install django==2.0.2`` 

Notice we are not using ``pip3`` but ``pip`` this is due to we are inside the our environment.
















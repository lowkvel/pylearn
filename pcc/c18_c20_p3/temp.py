# temp

# spec for the project
"""
We’ll write a web app called Learning Log 
that allows users to log the topics they’re interested in 
and to make journal entries as they learn about each topic. 

The Learning Log home page will describe the site 
and invite users to either register or log in. 

Once logged in, a user can create new topics, 
add new entries, and read and edit existing entries.
"""

# create and use a new venv
"""
Create a new directory for the project named new_dir
CD into the directory new_dir created above
Run the command "python -m venv new_venv_name" to create a new venv
Run the command "source new_venv_name/bin/activate" to activate the new venv
Run the command "deactivate" to deactivate the new venv if needed
* the new venv folder "new_venv_name" will be located under new_dir
"""

# install Django for the new venv
"""
Run the command "pip install django" to install Django on current venv
* the Django packages will be located under new_dir/new_venv_name/...
"""

# create a Django project under the new venv
"""
Run the command "django-admin startproject project_name ." to create a Django project
* the project folders "project_name" will be located under new_dir

The settings.py file controls how Django interacts with your system and manages your project. 
The urls.py file tells Django which pages to build in response to browser requests. 
The wsgi.py file helps Django serve the files it creates. The filename is an acronym for "web server gateway interface".
"""

# create the database for the project
"""
Run the command "python manage.py migrate" to create the database
"""

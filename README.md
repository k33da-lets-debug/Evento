# Evento Project

## Setup and running this project
 Make sure you have python 3.7 installed.
 
 1. Create a folder where you can store your project.
 2. After that go to that path in console(cmd/shell/bash/powershell)
 
    `cd path_to_your_local_folder`
 
 3. Clone this repository in that folder by typing
 
    `https://github.com/k33da-lets-debug/Evento.git`
 
 4. Install virtual environment:
    cd to `cd ./Evento/evento_django_project`
    `pip install virtualenv`
 
 5. Creating virtual environment:
    `virtualenv venv`
 
 6. Activating virtual environment:
    `.\venv\Scripts\activate.bat`
    Note: you will see (venv) on very left side of your console that means your virtual environment is now activate (or check it with 'pip freeze').
 
 7. Installing dependencies:
    Note: Check if you got "Evento\evento_django_project\dependencies.txt" inside your cloned folder.
 
    `pip install -r path_to_project_dependencies.txt`
 
 8. Running this project:
    First go to path where manage.py is located by typing
    `cd path_to_project_where_manage_dot_py_is_located`
 
    Now run this project by typing
    `python manage.py runserver`
    
    
 ##Structure of project
 Actual django project is inside evento_django_project\Project
 You can find settings folder which is used to separate local and production settings file(No need to cahange that)
 

 
 
 
 


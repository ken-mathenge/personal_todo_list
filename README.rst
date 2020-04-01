=========
Todo List
=========

A simple Django app to keep track of your todo list. It comes with a RESTful API, celery task queue, Oauth2 and is fully tested. It comes with its required dependancies such as Django, Django Rest Framework and Oauth2.

Features
--------

 - Django
 - Django Rest Framework
 - Oauth2
 - Django-Redis
 - Django-Celery

Prerequisites
-------------
 
 - Python >=3.6
 - Pip
 - Virtualenv

Installation
------------

1.Setup a local deploymnet environment::
	python3 -m venv {{ virtualenv_name }}
	source {{ virtualenv_name }}/bin/activate

2.Pip3 install the application::
	pip3 install todolist_v2

3.Run the applications server::
	todo_manage runserver

4.To remove the application::
	pip3 uninstall todolist_v2

License
-------
You can checkout the license here https://gitlab.slade360emr.com/training/mathenge-project/blob/master/LICENSE.
Thank You so much

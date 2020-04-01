import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='personal_todo_list',
    # version='1.0.21',
    packages=find_packages(),
    include_package_data=True,
    description='A simple Django app to keep track of my person todo list. It comes with a RESTful API, celery task queue, Oauth2 and is fully tested and monitoring with tools such as Grafana.',
    long_description=open('README.rst').read(),
    author='Kenneth Mathenge',
    author_email='mathenge@example.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        "Django~=3.0.4",
        "django-allauth~=0.41.0",
        "psycopg2~=2.8.4",
        "gunicorn~=20.0.4",
        "fabric3==1.14.post1",
        "sentry-sdk~=0.14.3",
        "whitenoise~=5.0.1",
        "twine~=3.1.1",
        "wheel~=0.34.2",
    ],
    scripts=['bin/todo_manage'],
)

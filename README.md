How-to Guide:

1. To run this django app on your PC at first i suggest you to install all pip dependencies:
    - cd to the directory where requirements.txt is located.
    - activate your virtualenv.
    - run: pip install -r requirements.txt in your shell.
    
2. Next step is to create your own superuser:
    - ./manage.py createsuperuser
    - type in your login name
    - type in your email (can be skipped)
    - type in your password
    
3. Here the database stuff will be explained (a bit later)



--------
To enable translations run:

    $ django-admin compilemessages -l ru
    
-------
To run celery app

- update requirements:

      
    $ pip install -r requirements.txt
   

- run worker in a terminal

   
    $ celery -A dishmaker worker --loglevel=info
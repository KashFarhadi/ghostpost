# Welcome to Django! GhostPost
Harness the power of django and the inter to Boast or Roast anyone or anything with complete anonymity. Did you love that chick-flick but afraid your bros would grill you for it? Do you secretly hate guac and fear being banished to guacless northern nation beyond the Niagra? Did someone surprise you with an act of kindness or you witness someone trash talking the glorious CyberTruck and wish repentance on them. Now you can let people know. It's kind of like reddit but for annonymous gossiping!

### Completed by
Kash Farhadi

## Running the Application

Fork, Clone, Navigate to directory
Create and start a a virtual environment

for pipenv:
`pipenv install`

`pipenv shell`

`python manage.py makemigrations {foldername}` 
(where foldername is the top level folder for this project)

`python manage.py migrate`

Create an admin account (superuser) if you would like to test admin features and access the admin page. Easily create users and objects from the built in django visual interface

`python manage.py createsuperuser`

Finally start the django server using: 
`python manage.py runserver`

Access the homepage at 
`http://127.0.0.1:8000/` 
`http://localhost:8000/`

Admin page
`http://127.0.0.1:8000/admin` 
`http://localhost:8000/admin`


##### Built using Python 3.8 and the latest version of Django (2.1.2 as of this writing)
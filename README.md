# University

Django project for managing students' assignments to optional courses.

## Check it out!

[University project deployed on Heroku](LINK)


## Installation

A quick introduction of the minimal setup:

Python3 must be already installed.

```shell
git clone https://github.com/KatyaVasylieva/university
cd university
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Set environment variables:

```shell
export SECRET_KEY='django-insecure-mft9u&!rrp@7_w5o5jvp6hrz&_o#ft6@hqbwys#u+3g2)^t4&u'
export DATABASE_URL="postgres://zlukijyb:KbP_iXPt69-mYsyHmXNX97zvqaJCK4tD@snuffleupagus.db.elephantsql.com/zlukijyb"
```

Choose one of the options:

```shell
export DJANGO_DEBUG=True # to run the server in debug mode
```

```shell
export DJANGO_DEBUG=False # for production
```

Run Django server:
```shell
python manage.py runserver
```

## Features

* Authentication functionality for Student(User)
* Create/update/delete functionality for courses and students directly from website interface
* Possibility to assign or remove User form particular course

## Demo
![Login interface](static/img/readme/login_demo.png)
![Home page interface](static/img/readme/home_demo.png)
![Home page interface](static/img/readme/home_lower_demo.png)
![List page interface](static/img/readme/course_list_demo.png)
![Detail page interface](static/img/readme/student_detail_demo.png)

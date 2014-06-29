city_suggest
============

django city suggest

Installation
------------
Download project:

    git clone https://github.com/abcdw/city_suggest

Configurate virtualenv and install requirements:

    rm -rf city_suggest_env/
    virtualenv city_suggest_env
    source city_suggest_env/bin/activate

    cd city_suggest/city_suggest
    pip install -r requirements.txt

Create and populate database with [django-cities-light](https://github.com/yourlabs/django-cities-light):

    ./manage.py syncdb
    ./manage.py cities_light

Run project and enjoy:

    ./manage.py runserver

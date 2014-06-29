city_suggest
============

django city suggest

Installation
------------
Download project :

    git clone https://github.com/abcdw/city_suggest

Enter project dir:

    cd city_suggest
    
Execute [./run.sh](https://github.com/abcdw/city_suggest/blob/master/run.sh) or do this stuff manual:

Configurate virtualenv and install requirements :

    rm -rf city_suggest_env/
    virtualenv city_suggest_env
    source city_suggest_env/bin/activate

    cd city_suggest
    pip install -r requirements.txt

Create and populate database with [django-cities-light](https://github.com/yourlabs/django-cities-light) :

    ./manage.py syncdb
    ./manage.py cities_light

Run project and enjoy [http://127.0.0.1:8000/suggest](http://127.0.0.1:8000/suggest) :

    ./manage.py runserver

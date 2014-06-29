rm -rf city_suggest_env/
virtualenv city_suggest_env
source city_suggest_env/bin/activate
cd city_suggest
pip install -r requirements.txt
./manage.py syncdb
./manage.py cities_light

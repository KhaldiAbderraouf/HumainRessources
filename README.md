# to install the project:

-clone repo:

git clone git@github.com:KhaldiAbderraouf/HumainRessources.git

cd HumainRessources

-add virtual environement:

python3 -m venv env

source env/bin/activate

-insrall requirements:

pip3 install -r requirements.txt

-migrate database:

python manage.py migrate

-add super user:

python manage.py createsuperuser --email admin@example.com --username admin

-run locally:

python manage.py runserver

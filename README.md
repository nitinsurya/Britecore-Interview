# Britecore-Interview
Web application

Following commands are to be run for the application to run:

virtualenv -p python3 server
cd server
source bin/activate
pip install -r requirements.txt
python db_setup.py

nohup ./api.py </dev/null &>/dev/null &
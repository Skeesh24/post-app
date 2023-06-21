apt install python3-venv &&
apt install python3-pip
apt install mysql-server
apt install libmysqlclient-dev
python3 -m pip install -U fastapi[all] &&
python3 -m pip install -U sqlalchemy &&
python3 -m pip install -U bcrypt &&
python3 -m pip install -U passlib &&
python3 -m pip install -U python-jose[cryptography] &&
python3 -m pip install -U alembic &&
python3 -m pip install -U mysql-connector-python &&
python3 -m pip install -U mysql &&
python3 -m pip install -U uvicorn
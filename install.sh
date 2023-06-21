apt install python3-venv &&
apt install python3-pip
"/bin/python3" -m pip install -U fastapi[all] &&
"/bin/python3" -m pip install -U mysql &&
"/bin/python3" -m pip install -U mysql-connector-python &&
"/bin/python3" -m pip install -U sqlalchemy &&
"/bin/python3" -m pip install -U bcrypt &&
"/bin/python3" -m pip install -U passlib &&
"/bin/python3" -m pip install -U python-jose[cryptography] &&
"/bin/python3" -m pip install -U alembic &&
"/bin/alembic" init && 
"/bin/alembic" upgdare 9714d366efca
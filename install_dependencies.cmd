py -3 -m venv &&
"./venv/Scripts/python.exe" -m pip install -U fastapi[all] &&
"./venv/Scripts/python.exe" -m pip install -U psycopg2 &&
"./venv/Scripts/python.exe" -m pip install -U sqlalchemy &&
"./venv/Scripts/python.exe" -m pip install -U bcrypt &&
"./venv/Scripts/python.exe" -m pip install -U passlib &&
"./venv/Scripts/python.exe" -m pip install -U python-jose[cryptography] &&
"./venv/Scripts/python.exe" -m pip install -U alembic &&
alembic init && 
alembic upgdare 9714d366efca
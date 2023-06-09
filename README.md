# post-app

this app are represents a backend of a small social net, gives u the ability to create entires, rate other people's entires and a little more features

## installation and deploy:

1. in the root dir create a venv like "py -3 -m venv <name>"
2. install dependencies:
   - "./venv/Scripts/python.exe" -m pip install -U fastapi[all]
   - "./venv/Scripts/python.exe" -m pip install -U psycopg2
   - "./venv/Scripts/python.exe" -m pip install -U sqlalchemy
   - "./venv/Scripts/python.exe" -m pip install -U bcrypt
   - "./venv/Scripts/python.exe" -m pip install -U passlib
   - "./venv/Scripts/python.exe" -m pip install -U python-jose[cryptography]
   - "./venv/Scripts/python.exe" -m pip install -U alembic
3. create the .env in the root dir sets constants: host, port, user, pwd, db_name, driver for database and JWT secret key for authentication
4. in the root dir init the alembic tool like "alembic init && alembic upgdare 4d0bd855"
5. run the server by exec start.cmd

**try it out:** _a link to the deployment_

# post-webapp

== based on framework fastAPI ==

installation and deploy:

1. in the root project dir create a venv like "py -3 -m venv <name>"
2. install dependencies:
   2.1 & "./venv/Scripts/python.exe" -m pip install -U fastapi[all]
   2.2 & "./venv/Scripts/python.exe" -m pip install -U psycopg2
   2.3 & "./venv/Scripts/python.exe" -m pip install -U sqlalchemy
   2.4 & "./venv/Scripts/python.exe" -m pip install -U bcrypt
   2.5 & "./venv/Scripts/python.exe" -m pip install -U passlib
3. create the config.py in the root dir sets db constants, like host, port, user, pwd, db_name and driver
4. run the server by exec start.cmd

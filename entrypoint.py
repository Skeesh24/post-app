from subprocess import call

# installing dependencies
call(['sh', './install.sh'])

# starting server
call(["sh", "./app/main.py"])

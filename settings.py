import os

Lines = open('.env', 'r').readlines()

for line in Lines:
    line = line.strip()
    os.environ[line[:line.find("=")]] = line[line.find("=") + 1:]
HOST = os.environ['HOST']
USER = os.environ['USER']
PASSWORD = os.environ['PASSWORD']

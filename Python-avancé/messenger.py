from datetime import datetime
from argparse import ArgumentParser

from remoteserver import Remoteserver
from localserver import Localserver
from client import Client
    
argument_parser = ArgumentParser()
argument_parser.add_argument('-f', '--filename')
argument_parser.add_argument('-u', '--url')
argument_parser.add_argument('-p', '--portail', action = 'store_true')
arguments = argument_parser.parse_args()
if arguments.filename is not None:
    server = Localserver(arguments.filename)
elif arguments.url is not None:
    server = Remoteserver(arguments.url)
else:
    print('Error: -f or -u should be set')
    exit(-1)

server.load_server()
client = Client(server) 
client.accueil()
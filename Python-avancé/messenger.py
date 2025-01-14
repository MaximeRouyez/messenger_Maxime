from datetime import datetime
from argparse import ArgumentParser

from model import User
from model import Channels
from model import Messages
from server import Server
from client import Client

class RemoteServer:
    def __init__(self, server_url):
        self.server_url= server_url
    
argument_parser = ArgumentParser()
argument_parser.add_argument('-f', '--filename')
argument_parser.add_argument('-u', '--url')
argument_parser.add_argument('-p', '--portail', action = 'store_true')
arguments = argument_parser.parse_args()
server: Server
if arguments.filename is not None:
    serveur = Server(arguments.filename)
elif arguments.url is not None:
    serveur = RemoteServer(arguments.url)
else:
    print('Error: -f or -u should be set')
    exit(-1)

server = Server.load_from_json_file(arguments.jsonfile) 
client = Client(server) 
client.accueil()
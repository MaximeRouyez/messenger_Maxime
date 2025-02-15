import requests
from model import User
from model import Channels
from model import Messages
from client import Client
from server import Server
import json

class Remoteserver:
    def __init__(self, url: str):
        self.url = url
        self.server = self
    
    def load_server(self):
        response1 = requests.get('https://groupe5-python-mines.fr/users')
        self.users = response1.json()
        response2 = requests.get('https://groupe5-python-mines.fr/channels')
        self.channels = response2.json()
        response3 = requests.get('https://groupe5-python-mines.fr/messages')
        self.messages = response3.json()
        server_with_classes = {'users': self.users,'channels': self.channels,'messages': self.messages}
        return server_with_classes
    
    def create_user(self, new_user:dict):
        requests.post('https://groupe5-python-mines.fr/users/create', json = new_user)
        
    def create_channels(self, new_channel:dict):
        requests.post('https://groupe5-python-mines.fr/channels/create', json = new_channel)
        
    def create_messages(self, new_message:dict):
        requests.post('https://groupe5-python-mines.fr/messages/create', json = new_message)
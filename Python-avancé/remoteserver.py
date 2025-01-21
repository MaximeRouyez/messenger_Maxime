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
    
    def load(self):
        pass
    
    def get_users(self):
        response = requests.get('https://groupe5-python-mines.fr/users')
        Users = response.json()
        return [Users.dico_to_user(user) for user in Users]
    
    def get_channels(self):
        response = requests.get('https://groupe5-python-mines.fr/channels')
        Channels = response.json()
        return [Channels.dico_to_user(channel) for channel in Channels]
        
    def create_user(self, new_user:dict):
        requests.post('https://groupe5-python-mines.fr/users/create', json = new_user)
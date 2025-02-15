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
        users_data = response1.json()
        self.users = [User(user['name'], user['id']) for user in users_data]
        response2 = requests.get('https://groupe5-python-mines.fr/channels')
        channels_data = response2.json()
        self.channels = [Channels(channel['id'], channel['name'], channel.get('member_ids', [])) for channel in channels_data]
        response3 = requests.get('https://groupe5-python-mines.fr/messages')
        messages_data = response3.json()
        self.messages = [Messages(message['id'], message['reception_date'], message['sender_id'], message.get('channel', None), message['content']) for message in messages_data]
        server_with_classes = {'users': self.users,'channels': self.channels,'messages': self.messages}
        return server_with_classes
    
    def save_server(self, server_with_classes):
        users_data = [user.to_dict() for user in server_with_classes['users']]
        channels_data = [channel.to_dict() for channel in server_with_classes['channels']]
        messages_data = [message.to_dict() for message in server_with_classes['messages']]
        response_user = requests.post('https://groupe5-python-mines.fr/users/create', json = {'users': users_data})
        requests.put('https://groupe5-python-mines.fr/channels/create', json={'channels': channels_data})
        requests.put('https://groupe5-python-mines.fr/messages/create', json={'messages': messages_data})
        if response_user.status_code == 200:
            print("✅ Channels mis à jour sur le serveur !")
        else:
            print(f"❌ Erreur lors de la mise à jour des channels : {response_user.text}")
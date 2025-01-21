from model import User
from model import Channels
from model import Messages
import json

class Localserver:
    def __init__(self, filename: str):
        self.filename = filename
        self.users: list[User] = []
        self.channels: list[Channels] = []
        self.messages: list[Messages] = [] 
    
    def load_server(self):
        with open (self.filename) as file:
            data= json.load(open(self.filename))
            self.users = [User(user['name'], user['id']) for user in data['users']]
            self.channels = [Channels(channel['id'], channel['name'], channel['member_ids']) for channel in data['channels']]
            self.messages = [Messages(message['id'], message['reception_date'], message['sender_id'], message['channel'], message['content']) for message in data['messages']]
        server_with_classes = {'users': self.users,'channels': self.channels,'messages': self.messages}
        return server_with_classes

    def save_server(self, server_with_classes):
        server_with_dicts = {}
        server_with_dicts['users'] = [user.to_dict() for user in server_with_classes['users']]
        server_with_dicts['channels'] = [channel.to_dict() for channel in server_with_classes['channels']]
        server_with_dicts['messages'] = [message.to_dict() for message in server_with_classes['messages']]
        with open(self.filename, 'w') as server_json_file:
            json.dump(server_with_dicts, server_json_file)
    
    def get_users(self) -> list[User]:
        return self.users
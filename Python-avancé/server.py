from model import User
from model import Channels
from model import Messages
from client import Client
import json
SERVER_FILE_PATH = 'server_json.json'

class Server:
    def __init__(self, users:list[User], channels:list[Channels], message:list[Messages]):
        self.users = users
        self.channels = channels
        self.message = message 
    
    def load_server(self):
        with open (SERVER_FILE_PATH) as file:
            server= json.load(file)
            users = [User(user['name'], user['id']) for user in server['users']]
            channels = [Channels(channel['id'], channel['name'], channel['member_ids']) for channel in server['channels']]
            messages = [Messages(message['id'], message['reception_date'], message['sender_id'], message['channel'], message['content']) for message in server['messages']]
        server_with_classes = {'users': users,'channels': channels,'messages': messages}
        return server_with_classes

    def save_server(server_with_classes):
        server_with_dicts = {}
        server_with_dicts['users'] = [user.to_dict() for user in server_with_classes['users']]
        server_with_dicts['channels'] = [channel.to_dict() for channel in server_with_classes['channels']]
        server_with_dicts['messages'] = [message.to_dict() for message in server_with_classes['messages']]
        with open(SERVER_FILE_PATH, 'w') as server_json_file:
            json.dump(server_with_dicts, server_json_file)
    
    def get_users(self) -> list[User]:
        return self.users
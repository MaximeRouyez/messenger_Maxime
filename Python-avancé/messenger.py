from datetime import datetime
import json
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s','--server')
parser.add_argument('-u','--url')
args =  parser.parse_args()

print('Le chemin du fichier est :',args.server)

SERVER_FILE_PATH = args.server

def load_server():
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

class User:
    def __init__(self, name: str, id: int):
        self.id = id
        self.name = name
    def __repr__(self):
        return f'User(name={self.name}, id={self.id}, )'
    def to_dict(self) -> dict:
        return {'id': self.id,'name': self.name}

class Channels:
    def __init__(self, id: int, name: str, member_ids: str):
        self.id = id
        self.name = name
        self.member_ids = member_ids
    def __repr__(self):
        return f'Channels(id={self.id}, name={self.name}, member_ids={self.member_ids})'
    def to_dict(self) -> dict:
        return {'id': self.id,'name': self.name,'member_ids': self.member_ids}

class Messages:
    def __init__(self, id: int, reception_date: str, sender_id: int, channel: int, content: str):
        self.id = id
        self.reception_date = reception_date
        self.sender_id = sender_id
        self.channel = channel
        self.content = content
    def __repr__(self):
        return f'Messages(id={self.id}, reception_date={self.reception_date}, sender_id={self.sender_id}, channel={self.channel}, content={self.content})'
    def to_dict(self) -> dict:
        return {'id': self.id,'reception_date': self.reception_date,'sender_id': self.sender_id,'channel': self.channel,'content': self.content}

def conversion_dico_user(dico):
    return User[dico['id'], dico['name']]

def conversion_dico_channels(dico):
    return Channels[dico['id'], dico['name'], dico['member_ids']]

def conversion_dico_messages(dico):
    return Messages[dico['id'], dico['reception_date'], dico['sender_id'], dico['channel'], dico['content']]

def start ():
    print('=== Messenger ===')
    print('x. Leave')
    print('1. See users')
    print('2. See channels')
    choice = input('Select an option and press <Enter>: ')
    if choice == 'x':
        print('Bye!')
    elif choice == '1':
        userscreen()
    elif choice == '2':
        channelscreen()

def userscreen ():
    print('Users:')
    server_with_classes = load_server()
    users: list[User] = server_with_classes['users']
    for user in users:
        print(user.id, '.', user.name)
    print('n. Create user')
    print('x. Main Menu')
    choice = input('Select an option and press <Enter>: ')
    if choice == 'x':
        start()
    elif choice == 'n':
        newuser()
    else:
        userscreen()

def channelscreen ():
    print('channels')
    server_with_classes = load_server()
    channels = server_with_classes['channels']
    for channel in channels:
        print(channel.id, '.', channel.name)
    print('x. Main Menu')
    print('n. Create channel')
    choice = input('Select an option and press <Enter>: ')
    if choice == 'x':
        start()
    elif choice == 'n':
        newchannel()
    else: 
        channelscreen()

def newchannel():
    server_with_classes = load_server()
    nomgrp = input('Select a name and press <Enter>: ')
    n_id = max(channel.id for channel in server_with_classes['channels']) + 1
    L=[]
    print('x. Leave')
    print('a. Add users')
    choice = input('Select an option and press <Enter>: ')
    if choice == 'a':
        nom = input('Select a name and press <Enter>: ')
        users: list[User] = server_with_classes['users']
        for user in users:
            if user.name == nom:
                L.append(user.id)
            else:
                n2_id = max(user.id for user in server_with_classes['users'])+1
                new_user = User(nom, n_id)
                server_with_classes['users'].append(new_user)
                L.append(n2_id)
        new_channel = Channels(n_id, nomgrp, L)
        server_with_classes['channels'].append(new_channel)
        save_server(server_with_classes)
    elif choice == 'x':
        channelscreen()
    else:
        channelscreen()
    accueil()

def newuser():
    server_with_classes = load_server()
    nom = input('Select a name and press <Enter>: ')
    n_id = max(user.id for user in server_with_classes['users']) + 1
    new_user = User(nom, n_id)
    server_with_classes['users'].append(new_user)
    save_server(server_with_classes)
    userscreen()

def accueil(): 
    print('=== Messenger ===')
    print('x. Leave')
    print('1. See users')
    print('2. See channels')
    choice = input('Select an option and press <Enter>: ')
    if choice == 'x':
        print('Bye!')
    elif choice== '1':
        userscreen()
    elif choice == '2':
        channelscreen()
    else :
        print('Unknown option:', choice)
        accueil()

accueil()

 #server = {
 #    'users': [
 #        {'id': 1, 'name': 'Alice'},
 #        {'id': 2, 'name': 'Bob'}
 #    ],
 #    'channels': [
 #        {'id': 1, 'name': 'Town square', 'member_ids': [1, 2]}
 #    ],
 #    'messages': [
 #        {
 #            'id': 1,
 #            'reception_date': datetime.now(),
 #            'sender_id': 1,
 #            'channel': 1,
 #            'content': 'Hi 👋'
 #        }
 #    ]
 #}
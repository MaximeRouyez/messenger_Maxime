from datetime import datetime
import json
def load_server():
    with open ('server_json.json') as file:
        server= json.load(file)
        users = [User(user['name'], user['id']) for user in server['users']]
        channels = [Channels(channel['id'], channel['name'], channel['member_ids']) for channel in server['channels']]
        messages = [Messages(message['id'], message['reception_date'], message['sender_id'], message['channel'], message['content']) for message in server['messages']]

    server_with_classes = {
        'users': users,
        'channels': channels,
        'messages': messages
    }
    return server_with_classes

class User:
    def __init__(self, name: str, id: int):
        self.id = id
        self.name = name
    def __repr__(self):
        return f'User(name={self.name}, id={self.id}, )'

    def to_dict(self) -> dict:
        '''Convertit un objet `user` de la classe `User` en `dict`.

        Exemple :
        >>> user_dict = user.to_dict()
        '''
        return {
            'id': self.id,
            'name': self.name
        }

class Channels:
    def __init__(self, id: int, name: str, member_ids: str):
        self.id = id
        self.name = name
        self.member_ids = member_ids
    def __repr__(self):
        return f'Channels(id={self.id}, name={self.name}, member_ids={self.member_ids})'

    def to_dict(self) -> dict:
        '''Convertit un objet `channel` de la classe `Channels` en `dict`.

        Exemple :
        >>> channel_dict = channel.to_dict()
        '''
        return {
            'id': self.id,
            'name': self.name,
            'member_ids': self.member_ids
        }

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
        '''Convertit un objet `message` de la classe `Messages` en `dict`.

        Exemple :
        >>> message_dict = message.to_dict()
        '''
        return {
            'id': self.id,
            'reception_date': self.reception_date,
            'sender_id': self.sender_id,
            'channel': self.channel,
            'content': self.content
        }

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
    # if choice == 'x':
    #     start()
    # elif choice == 'n':
    #     newuser()
    # else: 
    #     userscreen()

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
#     elif choice == 'n':
#         newchannel()
#     else: 
#         channelscreen()

# def newchannel():
#     nomgrp= input('Select a name and press <Enter>: ')
#     n_id = max(d['id'] for d in server['channels'])+1
#     L=[]
#     print('x. Leave')
#     print('a. Add users')
#     choice = input('Select an option and press <Enter>: ')
#     if choice == 'a':
#         nom = input('Select a name and press <Enter>: ')
#         for user in server['users']:
#             if user['name'] == nom:
#                 L.append(user['id'])
#             else:
#                 n2_id = max(d['id'] for d in server['users'])+1
#                 server['users'].append({'id': n2_id, 'name': nom})
#                 L.append(n2_id)
#     elif choice == 'x':
#         channelscreen()
#     else:
#         channelscreen()
#     server['channels'].append({'id': n_id, 'name': nomgrp, 'member_ids': L})
#     accueil()

# def newuser():
#     nom = input('Select a name and press <Enter>: ')
#     n_id = max(d['id'] for d in server['users'])+1
#     server['users'].append({'id': n_id, 'name': nom})
#     accueil()

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
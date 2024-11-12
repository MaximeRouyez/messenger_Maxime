from datetime import datetime
import json
def load_server():
    with open ('server_json.json') as file:
        server= json.load(file)

    return load_server()

class User:
    def __init__(self, name: str, id: int):
        self.id = id
        self.name = name

class Channels:
    def __init__(self, id: int, name: str, member_ids: str):
        self.id = id
        self.name = name
        self.member_ids = member_ids

class Messages:
    def __init__(self, id: int, reception_date: str, sender_id: int, channel: int, content: str):
        self.id = id
        self.reception_date = reception_date
        self.sender_id = sender_id
        self.channel = channel
        self.content = content

def conversion_dico_user(dico):
    return User[dico['id'], dico['name']]

def conversion_dico_channels(dico):
    return Channels[dico['id'], dico['name'], dico['member_ids']]

def conversion_dico_messages(dico):
    return Messages[dico['id'], dico['reception_date'], dico['sender_id'], dico['channel'], dico['content']]

# server = {
#     'users': [
#         {'id': 1, 'name': 'Alice'},
#         {'id': 2, 'name': 'Bob'}
#     ],
#     'channels': [
#         {'id': 1, 'name': 'Town square', 'member_ids': [1, 2]}
#     ],
#     'messages': [
#         {
#             'id': 1,
#             'reception_date': datetime.now(),
#             'sender_id': 1,
#             'channel': 1,
#             'content': 'Hi 👋'
#         }
#     ]
# }

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
    for user in server['users']:
        print(user['id'], '.', user['name'])
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
    for channel in server['channels']:
        print(channel['id'], '.', channel['name'])
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
    nomgrp= input('Select a name and press <Enter>: ')
    n_id = max(d['id'] for d in server['channels'])+1
    L=[]
    print('x. Leave')
    print('a. Add users')
    choice = input('Select an option and press <Enter>: ')
    if choice == 'a':
        nom = input('Select a name and press <Enter>: ')
        for user in server['users']:
            if user['name'] == nom:
                L.append(user['id'])
            else:
                n2_id = max(d['id'] for d in server['users'])+1
                server['users'].append({'id': n2_id, 'name': nom})
                L.append(n2_id)
    elif choice == 'x':
        channelscreen()
    else:
        channelscreen()
    server['channels'].append({'id': n_id, 'name': nomgrp, 'member_ids': L})
    accueil()

def newuser():
    nom = input('Select a name and press <Enter>: ')
    n_id = max(d['id'] for d in server['users'])+1
    server['users'].append({'id': n_id, 'name': nom})
    accueil()

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
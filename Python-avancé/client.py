from model import User
from model import Channels
from model import Messages
from server import Server

class Client:
    def __init__(self, server : Server):
        self.server = server
    def start (self):
        print('=== Messenger ===')
        print('x. Leave')
        print('1. See users')
        print('2. See channels')
        choice = input('Select an option and press <Enter>: ')
        if choice == 'x':
            print('Bye!')
        elif choice == '1':
            Client.userscreen()
        elif choice == '2':
            Client.channelscreen()

    def userscreen (self):
        print('Users:')
        server_with_classes = Server.load_server()
        users: list[User] = server_with_classes['users']
        for user in users:
            print(user.id, '.', user.name)
        print('n. Create user')
        print('x. Main Menu')
        choice = input('Select an option and press <Enter>: ')
        if choice == 'x':
            Client.start()
        elif choice == 'n':
            Client.newuser()
        else:
            Client.userscreen()

    def channelscreen (self):
        print('channels')
        server_with_classes = Server.load_server()
        channels = server_with_classes['channels']
        for channel in channels:
            print(channel.id, '.', channel.name)
        print('x. Main Menu')
        print('n. Create channel')
        choice = input('Select an option and press <Enter>: ')
        if choice == 'x':
            Client.start()
        elif choice == 'n':
            Client.newchannel()
        else: 
            Client.channelscreen()

    def newchannel(self):
        server_with_classes = Server.load_server()
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
            new_channel = Channels(n2_id, nomgrp, L)
            server_with_classes['channels'].append(new_channel)
            Server.save_server(server_with_classes)
        elif choice == 'x':
            Client.channelscreen()
        else:
            Client.channelscreen()
        Client.accueil()

    def newuser(self):
        server_with_classes = Server.load_server()
        nom = input('Select a name and press <Enter>: ')
        n_id = max(user.id for user in server_with_classes['users']) + 1
        new_user = User(nom, n_id)
        server_with_classes['users'].append(new_user)
        Server.save_server(server_with_classes)
        Client.userscreen()

    def accueil(self): 
        print('=== Messenger ===')
        print('x. Leave')
        print('1. See users')
        print('2. See channels')
        choice = input('Select an option and press <Enter>: ')
        if choice == 'x':
            print('Bye!')
        elif choice== '1':
            Client.userscreen()
        elif choice == '2':
            Client.channelscreen()
        else :
            print('Unknown option:', choice)
            Client.accueil()
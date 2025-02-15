from model import User
from model import Channels
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
            self.userscreen()
        elif choice == '2':
            self.channelscreen()

    def userscreen (self):
        print('Users:')
        server_with_classes = self.server.load_server()
        users: list[User] = server_with_classes['users']
        for user in users:
            print(user.id, '.', user.name)
        print('n. Create user')
        print('x. Main Menu')
        choice = input('Select an option and press <Enter>: ')
        if choice == 'x':
            self.start()
        elif choice == 'n':
            self.newuser()
        else:
            self.userscreen()

    def channelscreen (self):
        print('channels')
        server_with_classes = self.server.load_server()
        channels = server_with_classes['channels']
        for channel in channels:
            print(channel.id, '.', channel.name)
        print('x. Main Menu')
        print('n. Create channel')
        choice = input('Select an option and press <Enter>: ')
        if choice == 'x':
            self.start()
        elif choice == 'n':
            self.newchannel()
        else: 
            self.channelscreen()
        
    def newchannel (self):
        server_with_classes = self.server.load_server()
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
                    new_user = User(nom, n2_id)
                    L.append(n2_id)
            server_with_classes['users'].append(new_user)
            new_channel = Channels(n_id, nomgrp, L)
            server_with_classes['channels'].append(new_channel)
            self.server.save_server(server_with_classes)
        elif choice == 'x':
            self.channelscreen()
        else:
            self.channelscreen()
        self.accueil()

    def newuser(self):
        server_with_classes = self.server.load_server()
        nom = input('Select a name and press <Enter>: ')
        n_id = max(user.id for user in server_with_classes['users']) + 1
        new_user = User(nom, n_id)
        server_with_classes['users'].append(new_user)
        self.server.save_server(server_with_classes)
        self.userscreen()

    def accueil(self): 
        print('=== Messenger ===')
        print('x. Leave')
        print('1. See users')
        print('2. See channels')
        choice = input('Select an option and press <Enter>: ')
        if choice == 'x':
            print('Bye!')
        elif choice== '1':
            self.userscreen()
        elif choice == '2':
            self.channelscreen()
        else :
            print('Unknown option:', choice)
            self.accueil()
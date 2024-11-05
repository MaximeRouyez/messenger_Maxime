from datetime import datetime

server = {
    'users': [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'}
    ],
    'channels': [
        {'id': 1, 'name': 'Town square', 'member_ids': [1, 2]}
    ],
    'messages': [
        {
            'id': 1,
            'reception_date': datetime.now(),
            'sender_id': 1,
            'channel': 1,
            'content': 'Hi 👋'
        }
    ]
}

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
    n = len(server['users'])
    print('Users:')
    for i in range (n): 
        print(i+1, '.', server['users'][i]['name'])
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
    m = len(server['channels'])
    print('channels')
    for i in range (m):
        print(i+1, '.', server['channels'][i]['name'])
    print('x. Main Menu')
    print('n. Create channel')
    choice = input('Select an option and press <Enter>: ')
    if choice == 'x':
        start()
    else: 
        channelscreen()

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
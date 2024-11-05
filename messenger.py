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

print('=== Messenger ===')
print('x. Leave')
print('1. See users')
print('2. See channels')
choice = input('Select an option and press <Enter>: ')
if choice == 'x':
    print('Bye!')
elif choice== '1':
    n = len(server['users'])
    print('Users:')
    for i in range (n): 
        print(i+1, '.', server['users'][i]['name'])
    print('n. Create user')
    print('x. Main Menu')
    choice = input('Select an option and press <Enter>: ')
    if choice== 'n':
         choice = input('Select a name and press <Enter>: ')
         server['users']["id n+1"]= ""
elif choice == '2':
    m = len(server['channels'])
    print('channels')
    for i in range (m):
        print(i+1, '.', server['channels'][i]['name'])
else :
    print('Unknown option:', choice)

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

def userscreen ():
    n = len(server['users'])
    print('Users:')
    for i in range (n): 
        print(i+1, '.', server['users'][i]['name'])
    print('n. Create user')
    print('x. Main Menu')
    choice = input('Select an option and press <Enter>: ')
    if choice ==
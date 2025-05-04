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
        # self.server = self # À quoi sert cette ligne ?

    # Cette fonction est inutile. Vous n'avez pas besoin de télécharger
    # toutes les informations du serveur pour les garder en mémoire.
    # Il vaut mieux aller les chercher au cas par cas lorsque
    # vous en avez besoin, sinon vous n'aurez pas accès aux mises
    # à jour des autres utilisateurs.
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

    # J'ai extrait et adapté ces lignes de votre fonction `load_server`.
    # Remarquez qu'elle a la même signature (nombre et type des paramètres
    # et des valeurs de retour) que la fonction `Localserver.get_users`.
    # Ca permet au `Client`, qui va les utiliser, de ne pas avoir besoin de
    # savoir s'il utilise un `Localserver` ou un `Remoteserver` :
    # dans les 2 cas, il obtiendra une `list[User]` à jour.
    def get_users(self) -> list[User]:
        user_response = requests.get('https://groupe5-python-mines.fr/users')
        users_data = user_response.json()
        return [User(user['name'], user['id']) for user in users_data]

    # Cette fonction n'a pas le comportement attendu :
    # à chaque appel, elle crée un nouvel utilisateur, un nouveau channel,
    # et un nouveau message sur le serveur distant.
    # Il vaut mieux créer des fonctions unitaires `create_user`, `create_channel`,
    # `create_message` qui vous donneront un contrôle plus fin.
    def save_server(self, server_with_classes,):
        users_data = [user.to_dict() for user in server_with_classes['users']]
        channels_data = [channel.to_dict() for channel in server_with_classes['channels']]
        messages_data = [message.to_dict() for message in server_with_classes['messages']]
        response_user = requests.post('https://groupe5-python-mines.fr/users/create', json = users_data[-1])
        requests.post('https://groupe5-python-mines.fr/channels/create', json= channels_data[-1])
        requests.post('https://groupe5-python-mines.fr/messages/create', json= messages_data[-1])
        # Très bien de vérifier le status code !
        if response_user.status_code == 200:
            # Très bonne idée d'utiliser des emojis, c'est visuel
            print("✅ Channels mis à jour sur le serveur !")
        else:
            # Bonne utilisation des "f-string"
            print(f"❌ Erreur lors de la mise à jour des channels : {response_user.text}")

    def create_user(self, nom: str) -> None:
        user_creation_response = requests.post(f"{self.url}/users/create",json={"name": nom})
        if user_creation_response.status_code == 200:
            print("✅ Utilisateur créé sur le serveur !")
        else:
            print(f"❌ Erreur lors de la création d'un utilisateur : {user_creation_response.text}")

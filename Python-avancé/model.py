class User:
    def __init__(self, name: str, id: int):
        self.id = id
        self.name = name
    def __repr__(self):
        return f'User(name={self.name}, id={self.id}, )'
    def to_dict(self) -> dict:
        return {'id': self.id,'name': self.name}
    def conversion_dico_user(dico):
        return User[dico['id'], dico['name']]
    def conversion_user_dico(self):
        return {'id': self.id, 'name': self.name}

class Channels:
    def __init__(self, id: int, name: str, member_ids: str):
        self.id = id
        self.name = name
        self.member_ids = member_ids
    def __repr__(self):
        return f'Channels(id={self.id}, name={self.name}, member_ids={self.member_ids})'
    def to_dict(self) -> dict:
        return {'id': self.id,'name': self.name,'member_ids': self.member_ids}
    def conversion_dico_channels(dico):
        return Channels[dico['id'], dico['name'], dico['member_ids']]
    def conversion_channels_dico(self):
        return {'id': self.id, 'name': self.name, 'member_ids': self.member_ids}

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
    def conversion_dico_messages(dico):
        return Messages[dico['id'], dico['reception_date'], dico['sender_id'], dico['channel'], dico['content']]
    def conversion_messages_dico(self):
        return {'id': self.id,'reception_date': self.reception_date,'sender_id': self.sender_id,'channel': self.channel,'content': self.content}
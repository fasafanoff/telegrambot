from Chat import Chat


class Chats:


    def __init__(self):
        self.chats = {}

    def inc_user(self,chat_id,user,date):
        if chat_id not in self.chats:
            self.chats[chat_id] = Chat()
        self.chats[chat_id].inc_user(user,date)
    
    def includes(self,chat_id):
        return chat_id in self.chats

    def get_chat(self,chat_id) -> Chat:
        return self.chats[chat_id]
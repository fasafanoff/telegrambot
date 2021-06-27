class ChatInfo:




    def __init__(self):
        self.chat={}

    def inc_user(self,user):
        print(self.chat)
        user_id = user.id
        if user_id not in self.chat:
            self.chat[user_id] = {"user":user,"messages" : 0} 
        self.chat[user_id]["messages"] += 1



    def get_messages(self,user_id):
        return self.chat[user_id]["messages"]

    def get_user(self,user_id):
        return self.chat[user_id]["user"]

    def __repr__(self) -> str:
        result_string  = ""
        for user_id in self.chat : 
            number_of_messages = self.get_messages(user_id)
            result_string += str(self.get_user(user_id).username) + " has " +str(number_of_messages) + " message(s)\n"
        return result_string

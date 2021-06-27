from ChatInfo import ChatInfo
from utils import floor_date


class Daily:

    def __init__(self):
        self.daily = {}

    


    def inc_user(self,user,message_date):

        date_key = floor_date(message_date)


        if date_key not in self.daily:
            self.daily[date_key] = ChatInfo()
        self.daily[date_key].inc_user(user)


        print(self.daily)

    
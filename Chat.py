from telebot.types import Dictionaryable
from Daily import Daily
from ChatInfo import ChatInfo


class Chat:


    def __init__(self):
        self.alltime = ChatInfo()
        self.daily = Daily()
        # self.weekly
        # self.monthly
        # self.annually 

    

    def inc_user(self,user,date):
        self.alltime.inc_user(user)
        self.daily.inc_user(user,date)


    def __repr__(self) -> str:
        return str(self.alltime)

    def get_daily(self):
        return self.daily.daily

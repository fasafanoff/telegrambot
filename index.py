from datetime import date
from utils import load_obj, save_obj
from Chats import Chats
import telebot
import matplotlib.pyplot as plt





bot = telebot.TeleBot("1887909958:AAHad8fc4AAwUsylyYQkW19Z3E-Eyp8iss0", parse_mode=None)




try:
    chats = load_obj("chats")
except:
    chats = Chats()

@bot.message_handler(commands=['gdaily'])
def graph(message):
    pass 


@bot.message_handler(commands=['gall'])
def graph(message):


    chat_id = message.chat.id

    
    user_id = message.from_user.id
    chat = chats.get_chat(chat_id)

    daily = chat.get_daily()

    

    x = []

    y = []
    for day in daily:
        x.append(date.fromtimestamp(day))
        
        y.append(daily[day].get_messages(user_id))  


   
    
    
    # plotting the points 
    plt.plot(x, y)
    
    # naming the x axis
    plt.xlabel('day')
    # naming the y axis
    plt.ylabel('number of messages')
    
   
    

    plt.savefig('plot.png')

    img = open('plot.png', 'rb')
    bot.send_photo(chat_id,img)
    img.close()



    


@bot.message_handler(commands=['stats'])
def send_stats(message):

    chat_id = message.chat.id

    if not chats.includes(chat_id):
        return bot.send_message(chat_id,"No statistics to be sent!")

    chat = chats.get_chat(chat_id)
    bot.send_message(message.chat.id,str(chat))
    






@bot.message_handler(func=lambda m: True,content_types=["text", "sticker", "photo", "audio"])
def inc_messages(message):
    






    chat_id = message.chat.id
    user = message.from_user
    chats.inc_user(chat_id,user,message.date)

    save_obj(chats,"chats")


    




bot.polling(none_stop=True)


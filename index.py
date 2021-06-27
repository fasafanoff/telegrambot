from Plots import Plots
from apikey import APIKEY
from datetime import date
from utils import load_obj, save_obj
from Chats import Chats
import telebot
import matplotlib.pyplot as plt





bot = telebot.TeleBot(APIKEY, parse_mode=None)




try:
    chats = load_obj("chats")
except:
    chats = Chats()

@bot.message_handler(commands=['gall'])
def graph(message):
    pass 


@bot.message_handler(commands=['gdaily'])
def graph(message):

    chat_id = message.chat.id

    

    chat = chats.get_chat(chat_id)

    daily = chat.get_daily()




    plots = Plots()

    for day_id in daily.daily:        
        day = daily.get_day(day_id)
        
        for user_id in day.chat:

            plots.push(day.get_user(user_id),date.fromtimestamp(day_id),day.get_messages(user_id))



    fig = plt.figure()

    axes = fig.add_axes([0, 0, 1, 1])

    plots.plot(axes)
    

    plt.savefig('plot.png')
    plt.close()

    img = open('plot.png', 'rb')
    bot.send_photo(chat_id,img)
    img.close()



    


@bot.message_handler(commands=['stats'])
def send_stats(message):

    if(message.text == "") :
        return

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


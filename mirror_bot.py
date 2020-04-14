import telepot
import time

bot = telepot.Bot('TOKEN')

def handle(msg):
    content_type,chat_type,chat_id = telepot.glance(msg)
    if content_type == 'text':
        bot.sendMessage(chat_id,"you said {}".format(msg["text"]))

bot.message_loop(handle)
print ('Listening ...')
while 1:
    time.sleep(10)

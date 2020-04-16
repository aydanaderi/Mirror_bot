import telepot
import time

bot = telepot.Bot('TOKEN')

def mirror(msg):
    content_type,chat_type,chat_id = telepot.glance(msg)
    if content_type == 'text':
        bot.sendMessage(chat_id,"you said {}".format(msg["text"]))

bot.message_loop(mirror)
print ('waiting ...')
while 1:
    time.sleep(10)

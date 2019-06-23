import telepot, time
from pprint import pprint
from telepot.loop import MessageLoop
import rss

token = "811836671:AAHTTjuoRK1eNAhsPZoFRey8iLi1L_PGJAA" # print("token: " token = input()
chatid = 366415230 # print("chat_id: ") chatid = input()
bot = telepot.Bot(token)
botMe = bot.getMe()


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text' and msg["text"] == '/update':
        bot.sendMessage(chat_id, rss.getLastEntry()["summary"], parse_mode="html")

def sendNew():
    print()

m = MessageLoop(bot, handle).run_as_thread()


while 1:
    time.sleep(5)

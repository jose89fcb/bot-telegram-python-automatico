# pip install python-telegram-bot==12.0.0
from telegram.ext import Updater
from telegram.ext import CommandHandler
updater = Updater('AQUI EL BOT_TOKEN')

def start(bot, update):

    
  
    chat_id = update.message.chat_id
    
    update.message.reply_text('Tú ID es: {}'.format(update.message.chat_id))

    

    
    

start_command = CommandHandler('start',start)
updater.dispatcher.add_handler(start_command)
updater.start_polling()

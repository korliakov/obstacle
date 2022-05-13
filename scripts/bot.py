#!/home/common/studtscm05/anaconda3/bin/python3

from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import os
  
updater = Updater("5382913323:AAHQwt3xvo6S_mHbQril6rg5sglL804Zmzw",
                  use_context=True)
  
  
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Привет. Напиши \help чтобы узнать больше.")
  
def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Доступные команды: 
    /check_plots - проверит, досчитались ли все данные 
    /get_plots - отправит графики
    """)
  

  
def check_plots(update: Update, context: CallbackContext):
    
    flag = os.popen("squeue | grep lmp_mpi").read()
    
    if flag:
        
        update.message.reply_text("Еще не досчиталось")
    else:
        update.message.reply_text("Все досчиталось")
        
def get_plots(update: Update, context: CallbackContext):
    
    for file in os.listdir("/home/common/studtscm05/obstacle/obstacle/data/plots"):
        context.bot.sendPhoto(update.effective_chat.id, photo=open("/home/common/studtscm05/obstacle/obstacle/data/plots/"+file, 'rb'))

  
  

  
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)
  
  
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)
  
  
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('check_plots', check_plots))
updater.dispatcher.add_handler(CommandHandler('get_plots', get_plots))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands
  
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
  
updater.start_polling()
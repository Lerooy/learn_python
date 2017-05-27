from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def show_error(bot, update, error):
    print(error)

def greet_user(bot, update):
    txt = 'Вызван /start'
    print(txt)
    print(update)
    update.message.reply_text(txt)
    # bot.sendMessage(update.message.chat_id, text='Давай общаться!')

def main():
    updater = Updater('384288897:AAEJaqrftnh8YHknddlNaaFGsbB8hZDLvy4')
    
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))

    updater.start_polling()
    updater.idle()

main()
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot,update):
    print(update)
    text_cmd='Вызван /start'
    print(text_cmd)

    text_greet="""Привет {}!
Я простой бот и понимаю только команду {}
""".format(update.message.chat.first_name, '/start')
    logging.info('Пользователь {} нажал /start'.format(update.message.chat.username))
    update.message.reply_text(text_greet)

def talk_to_me(bot, update):
    user_text = update.message.text
    logging.info(user_text)
    update.message.reply_text(user_text)

def main():
    updtr=Updater(settings.TELEGRAM_API_KEY)

    dp=updtr.dispatcher
    dp.add_handler(CommandHandler("start",greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    updtr.start_polling()
    updtr.idle()


if __name__=="__main__":
    logging.info('Bot started')
    main()

 
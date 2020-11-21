import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

with open('TOKEN') as f:
    token = f.readline()


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


updater = Updater(token)

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()
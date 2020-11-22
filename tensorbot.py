import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

class Tensorbot:

    def __init__(self):
        with open('TOKEN') as f:
            token = f.readline()
        
        self.tracked_variables = list()
        self.subscribed_users = list()
        
        self.updater = Updater(token, use_context=True)
        self.updater.dispatcher.add_handler(CommandHandler('hello', self.hello))
        self.updater.dispatcher.add_handler(CommandHandler('start', self.start))
        self.updater.dispatcher.add_handler(CommandHandler('help', self.printhelp))
        self.updater.dispatcher.add_handler(CommandHandler('update', self.update))
        self.updater.dispatcher.add_handler(CommandHandler('subscribe', self.subscribe))
        self.updater.dispatcher.add_handler(CommandHandler('unsubscribe', self.unsubscribe))
        self.updater.start_polling()
        # self.updater.idle()

    def subscribe(self, update, context):
        chat = update.effective_chat
        self.subscribed_users.append(chat)
        update.message.reply_text("Done! You'll get updates from me")
    
    def unsubscribe(self, update, context):
        chat = update.effective_chat
        self.subscribed_users.remove(chat)
        print("You won't receive any more updates")

    def hello(self, update, context):
        update.message.reply_text(f'Hello {update.effective_user.first_name}')

    def start(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

    def printhelp(self, update, context):
        update.message.reply_text("No help yet, tough luck!")

    def update(self, update, context):
        printstring = ""
        if len(self.tracked_variables) == 0:
            update.message.reply_text("No registered variables")
        else:
            for v in self.tracked_variables:
                printstring.append(f"{v.name}: {v.printvalue()}\n")
            update.message.reply_text(printstring)

    def register_variable(self, name, variable, autoupdate=False):
        var = Variable(name, variable, self, autoupdate=autoupdate)
        self.tracked_variables.append(var)
        return var

    def autoupdate(self, updatestring):
        for user in self.subscribed_users:
            user.send_message(updatestring)


class Variable:
    '''
     generic variable implementation
    '''
    
    def __init__(self, name, variable, bot_instance, autoupdate=False):
        self.name = name
        self.variable = variable
        self.autoupdates = autoupdate
        self.bot_instance = bot_instance
    
    def printvalue(self):
        return self.variable

    def update(self, variable):
        self.variable = variable
        if self.autoupdates:
            self.bot_instance.autoupdate(f"(auto)   {self.name}: {self.printvalue()}")

if __name__== '__main__':
    bot = Tensorbot()
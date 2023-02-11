"""
  Communication is everything! The availability of communication makes this part of our life more fun. For my little study of Python modules, I decided to study the topic of creating telegram bots a little. And in this small code, I will try to analyze the capabilities of the python-telegram-bot library.
  I will try to disassemble and install the library itself, set up the logging module, connect the bot with the telegram token and write a simple hello command.
"""
# First, let's install the required library. 

import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes

# Next, you need to configure the logging module. The essence of this module is to maintain an error log.

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Since the bot should in theory be hosted on a server and work with asynchronous frameworks, I will use asynchronous I/O. 
# Need to configure the module that will be responsible for the start command, which will display a welcome message. This function will receive two parameters: an update object which contains all information and data coming from telegram itself and a context object which is another object which contains information and data about the state of the library itself.The following functions will be configured in a similar way

async def start (update: Update, context: ContextTypes.DEFAULT_TYPE):
  await context.bot.send_message(chat_id=update.effective_chat.id, text =" My bot welcomes you!\n\n Want to see a list of commands! Click /help.")

async def help (update: Update, context: ContextTypes.DEFAULT_TYPE):
  await context.bot.send_message(chat_id=update.effective_chat.id, text ="You can enter the following commands:\n /git - Show my github link\n /mail - Show my mail\n /repl - show link to replit")

async def git (update: Update, context: ContextTypes.DEFAULT_TYPE):
   await context.bot.send_message(chat_id=update.effective_chat.id, text ="https://github.com/Drevlyanin")

async def mail (update: Update, context: ContextTypes.DEFAULT_TYPE):
   await context.bot.send_message(chat_id=update.effective_chat.id, text ="andrey.pavlyuk.2000@gmail.com")

async def repl (update: Update, context: ContextTypes.DEFAULT_TYPE):
   await context.bot.send_message(chat_id=update.effective_chat.id, text ="https://replit.com/@AndrewPavlyuk")

# The most important thing is to set up the interaction between our code and the telegram bot. To do this, we need to create an Application object. Replace 'TOKEN' with the bot's API token.

if __name__ == '__main__':
    application = ApplicationBuilder().token('TOKEN').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    help_handler = CommandHandler('help', help)
    application.add_handler(help_handler)

    git_handler = CommandHandler('git', git)
    application.add_handler(git_handler)

    mail_handler = CommandHandler('mail', mail)
    application.add_handler(mail_handler)

    repl_handler = CommandHandler('repl', repl)
    application.add_handler(repl_handler)

  
    application.run_polling()
"""
  Communication is everything! The availability of communication makes this part of our life more fun. For my little study of Python modules, I decided to study the topic of creating telegram bots a little. And in this small code, I will try to analyze the capabilities of the python-telegram-bot library.
  I will try to disassemble and install the library itself, set up the logging module, connect the bot with the telegram token and write a simple hello command.
"""
# First, let's install the required library. 

import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, CallbackQueryHandler, CallbackContext

# Next, you need to configure the logging module. The essence of this module is to maintain an error log.

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Since the bot should in theory be hosted on a server and work with asynchronous frameworks, I will use asynchronous I/O. 
# Need to configure the module that will be responsible for the start command, which will display a welcome message. This function will receive two parameters: an update object which contains all information and data coming from telegram itself and a context object which is another object which contains information and data about the state of the library itself.The following functions will be configured in a similar way

async def start(update: Update, context: CallbackContext):
    keyboard = [
        [KeyboardButton('/help')]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="My bot welcomes you!", reply_markup=reply_markup)

async def help(update: Update, context: CallbackContext):
    keyboard = [
        [KeyboardButton('/git'), KeyboardButton('/mail')],
        [KeyboardButton('/repl')]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="You can enter the following commands:", reply_markup=reply_markup)

async def git(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="https://github.com/Drevlyanin")

async def mail(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="andrey.pavlyuk.2000@gmail.com")

async def repl(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="https://replit.com/@AndrewPavlyuk")

async def git_button(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="https://github.com/Drevlyanin")

async def mail_button(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="andrey.pavlyuk.2000@gmail.com")

async def repl_button(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="https://replit.com/@AndrewPavlyuk")

# The most important thing is to set up the interaction between our code and the telegram bot. To do this, we need to create an Application object. Replace 'TOKEN' with the bot's API token.

if __name__ == '__main__':
    application = ApplicationBuilder().token('6175137571:AAHG_srBxtfN78bFMCygJKKxHkba111SrZc').build()
    
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

    git_button_handler = MessageHandler(filters.Regex('^/git$'), git_button)
    application.add_handler(git_button_handler)

    mail_button_handler = MessageHandler(filters.Regex('^/mail$'), mail_button)
    application.add_handler(mail_button_handler)

    repl_button_handler = MessageHandler(filters.Regex('^/repl$'), repl_button)
    application.add_handler(repl_button_handler)

    application.run_polling()

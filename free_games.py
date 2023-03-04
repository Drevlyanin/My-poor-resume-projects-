'''
In this bot, I made a small review on the telegram api and tried to write a simple code to get information about the distribution of free games in steam, epigames, gog.
'''

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import requests
from bs4 import BeautifulSoup


TOKEN = ''

def get_free_games():
    games = []

    # Steam
    url = 'https://steamdb.info/sales/?min_discount=95&min_rating=0'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for game in soup.find_all('tr', {'class': 'app'}):
        name = game.find('td', {'class': 'app-name'}).find('a').text.strip()
        discount = game.find('td', {'class': 'discount'}).text.strip()
        link = f"https://store.steampowered.com/app/{game['data-appid']}"
        games.append(f"{name} ({discount}) - {link}")

    # GOG
    url = 'https://www.gog.com/partner/stay_at_home'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for game in soup.find_all('div', {'class': 'free-game__content'}):
        name = game.find('div', {'class': 'free-game__title'}).text.strip()
        link = f"https://www.gog.com{game.find('a')['href']}"
        games.append(f"{name} - {link}")

    # Epic Games
    url = 'https://www.epicgames.com/store/free-games'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for game in soup.find_all('div', {'class': 'css-l2wjgv'}):
        name = game.find('div', {'class': 'css-0'}).text.strip()
        link = f"https://www.epicgames.com{game.find('a')['href']}"
        games.append(f"{name} - {link}")

    return games


def free_games(update, context):
    games = get_free_games()
    keyboard = []
    for i, game in enumerate(games):
        keyboard.append([InlineKeyboardButton(f"Game {i+1}", callback_data=f"game_{i}")])
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Select a game:", reply_markup=reply_markup)


def button(update, context):
    query = update.callback_query
    games = get_free_games()
    game_number = int(query.data.split('_')[1])
    context.bot.send_message(chat_id=query.message.chat_id, text=games[game_number])


updater = Updater(TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler('freegames', free_games))
updater.dispatcher.add_handler(CallbackQueryHandler(button))

updater.start_polling()
updater.idle()

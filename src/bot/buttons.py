import asyncio
import logging
import sys
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from os import getenv
from dotenv import load_dotenv













def start(update, context):
    keyboard = [
        [InlineKeyboardButton("Кнопка 1", callback_data= '1'),
        InlineKeyboardButton("Кнопка 2", callback_data='2')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Выберите кнопку:', reply_markup=reply_markup)


def button(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"Вы нажали кнопку: {query.data}")
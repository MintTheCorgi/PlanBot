from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup


start_router = Router()


@start_router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer(text="Здраствуйте, Рад приветсвовать вас! Я интерактивный помощник для вашего расписания. Создайте новую доску для начала работы.", reply_markup=main_kb(message.from_user.id))


def main_kb(user_telegram_id: int) -> ReplyKeyboardMarkup:
    kb_list: list[list[KeyboardButton]] = [
        [KeyboardButton(text="Создать новую доску"), KeyboardButton(text="Создать постоянную доску")],
        [KeyboardButton(text="Посмотреть активные доски"), KeyboardButton(text="Информация")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True, one_time_keyboard=False)

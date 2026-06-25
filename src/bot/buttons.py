from aiogram import Router, F, html
from aiogram.types import KeyboardButton, Message, inline_keyboard_markup
from aiogram.filters import CommandStart


start_router = Router()


@start_router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer(text="asd", reply_markup=main_kb(message.from_user.id))

async def main_kb(user_telegram_id: int) -> None:
    kb_list: list[list[KeyboardButton]] = [
        [KeyboardButton(text="Создать новую доску"), KeyboardButton(text="Создать постоянную доску")],
        [KeyboardButton(text="Посмотреть активные доски"), KeyboardButton(text="Информация")]
    ]
    keyboard = inline_keyboard_markup(keyboard=kb_list, resize_keyboard=True, one_time_keyboard=False)
    return keyboard
from aiogram import Router
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

router = Router()

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Кнопка 1", callback_data="1"),
        InlineKeyboardButton(text="Кнопка 2", callback_data="2"),
    ]
])


@router.callback_query()
async def button_handler(query: CallbackQuery) -> None:
    await query.answer()
    await query.message.edit_text(text=f"Вы нажали кнопку: {query.data}")

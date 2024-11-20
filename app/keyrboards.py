from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

goods = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Холодильник'), KeyboardButton(text='Водонагреватель'), KeyboardButton(text='Смарт-часы')],
    [KeyboardButton(text='Ноутбук'), KeyboardButton(text='Сотовый телефон'), KeyboardButton(text='МФУ')],
], resize_keyboard=True, input_field_placeholder='Выберите товар')

buy = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Купить'), KeyboardButton(text='Назад')]
], resize_keyboard=True, input_field_placeholder='Подтверждение заказа')

сonfirm = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Подтвердить заказ'), KeyboardButton(text='Назад')]
], resize_keyboard=True, input_field_placeholder='Подтверждение заказа')
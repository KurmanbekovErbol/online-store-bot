from aiogram import types, F, Router
from aiogram.filters import CommandStart
from app.keyrboards import *

router = Router()

@router.message(CommandStart())
async def command_start(message: types.Message):
    await message.answer('Добро пожаловать в наш онлайн-магазин', reply_markup=goods)

@router.message(F.text == 'Назад')
async def echo(message: types.Message):
    await message.answer('👈', reply_markup=goods)

@router.message(F.text == 'Купить')
async def echo(message: types.Message):
    await message.answer('Подтверждение заказа', reply_markup=сonfirm)

@router.message(F.text == 'Подтвердить заказ')
async def echo(message: types.Message):
    await message.answer('Благодарим за покупку', reply_markup=goods)

@router.message(F.text == 'Холодильник')
async def echo(message: types.Message):
    await message.reply_photo('https://www.kivano.kg/images/product/83699/full/1599638065_15717800.jpg', '''Холодильник Artel HD 276FN S-WH
16790 сом''', reply_markup=buy)

@router.message(F.text == 'Водонагреватель')
async def echo(message: types.Message):
    await message.reply_photo('https://www.kivano.kg/images/product/142212/full/1732020930_55902400.jpg','''Водонагреватель Ballu BWH/S 30 Orfeus DH
7450 сом''', reply_markup=buy)

@router.message(F.text == 'Смарт-часы')
async def echo(message: types.Message):
    await message.reply_photo('https://www.kivano.kg/images/product/141844/full/1730224514_98262100.jpg', '''Смарт-часы Samsung Galaxy Watch Ultra Titanium Gray
46400 сом''', reply_markup=buy)

@router.message(F.text == 'Ноутбук')
async def echo(message: types.Message):
    await message.reply_photo('https://www.kivano.kg/images/product/110698/full/1662549063_66628300.jpg', '''Ноутбук Lenovo V15 Intel Celeron N4020 4GB DDR 120GB SSD HD DOS Gray
18480 сом''', reply_markup=buy)

@router.message(F.text == 'Сотовый телефон')
async def echo(message: types.Message):
    await message.reply_photo('https://www.kivano.kg/images/product/140693/full/1727168899_57147000.png','''Сотовый телефон Google Pixel 9 256GB кремовый
90510 сом''', reply_markup=buy)

@router.message(F.text == 'МФУ')
async def echo(message: types.Message):
    await message.reply_photo('https://www.kivano.kg/images/product/106807/full/1653045832_95165500.jpg','''МФУ Canon i-Sensys MF3010
21850 сом''', reply_markup=buy)
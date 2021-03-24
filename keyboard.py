from telebot import types



startmenu = types.ReplyKeyboardMarkup(True, True)
startmenu.row('О себе', 'Мои работы')
startmenu.row('Контакты')




keyboard = types.InlineKeyboardMarkup(row_width=1)
keyboard.add(
	types.InlineKeyboardButton(text='В начало', callback_data='mainmenu')
	)





examples = types.InlineKeyboardMarkup(row_width=1)
examples.add(
	types.InlineKeyboardButton(text='Бот для ресторана', url='https://t.me/susisusisusibot', callback_data='susbut1'),
    types.InlineKeyboardButton(text='Гарант-бот', url='https://t.me/suppotibot', callback_data='susbut2'),
    types.InlineKeyboardButton(text='В начало', callback_data='mainmenu')
	)





contacts = types.InlineKeyboardMarkup(row_width=1)
contacts.add(
	types.InlineKeyboardButton(text='Я в Телеграм', url='https://t.me/whiteyod', callback_data='button1'),
	types.InlineKeyboardButton(text='Профиль на Кворк', url='https://kwork.ru/user/whiteyod', callback_data='button2'),
	types.InlineKeyboardButton(text='Мой GitHub', url='https://github.com/whiteyod', callback_data='button3'),
	types.InlineKeyboardButton(text='В начало', callback_data='mainmenu')
	)
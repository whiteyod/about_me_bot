import telebot

from telebot import types

import keyboard as kb



TOKEN = '1774773963:AAHjVZzAwCTQKZnAGutHrFDEE_JHD540sH4'

PHOTOME = 'AgACAgIAAxkBAANyYFsI35xU2aAVpXsj9kyO7dOcq4YAAkSxMRtjedhK_AABTNHm5HjWnMJNoi4AAwEAAwIAA3kAA_I7AAIeBA'
PHOTOSUSI = 'AgACAgIAAxkBAANzYFsJMlR-xRX0BBdE3BfUoVIp_1gAArC1MRv0YdhKkLJQa9Q_Y_oPwk2iLgADAQADAgADeAADRToAAh4E'
PHOTOEX = 'AgACAgIAAxkBAAOyYFsQB0Y2JQdj9rS3ZJQh4HWpLQMAAlGxMRtjedhKek1j7O0ijwcUiIedLgADAQADAgADeQADCzAAAh4E'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Приветствую Вас!\nЭтот бот создан чтобы рассказать Вам немного обо мне.', reply_markup=kb.startmenu)




@bot.message_handler(content_types=['text'])
def aboutMe(message):
    if message.text == 'О себе':
        bot.send_photo(
            message.chat.id,
            PHOTOME,
            caption= '''
            Меня зовут Ростислав, мне 24 года, я занимаюсь разработкой приложений на Python уже более года.\nЗа это время успел поучаствовать в трёх крупных проектах на Django.
            \nПараллельно этому изучил проектирование чертежей в ASKON и продолжаю изучать 3D-моделирование.\nСтараюсь развиваться сразу в нескольких сферах, чтобы стать специалистом во всех интересующих меня вещах.
            \nБуду рад помочь вам в решении ваших проблем.
            ''',
            reply_markup=kb.keyboard
            )

   
    elif message.text == 'Мои работы':
        bot.send_photo(message.chat.id, PHOTOEX, caption='Вот примеры моих последних работ:', reply_markup=kb.examples)

    elif message.text == 'Контакты':
        bot.send_message(message.chat.id, 'Способы связаться со мной и ещё некоторые ссылки\nТак же мой Email для связи:\n whiteyod@icloud.com', reply_markup=kb.contacts)





@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    if c.data == 'mainmenu':
        start(c.message)
    elif c.data == 'contactss':
        bot.send_message(c.message.chat.id, 'Способы связаться со мной и ещё некоторые ссылки\nТак же мой Email для связи:\n whiteyod@icloud.com', reply_markup=kb.contacts)

bot.polling()


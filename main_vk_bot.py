from random import randint

import vk_api
from vk_bot import VkBot
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

from config import CONST_TOKEN, HOLIDAY_DAY, HOLIDAY_NAME


# Для config
def set_season_holidays(left, right):
    season = ''
    for i in range(left, right):
        season += str(list(HOLIDAY_DAY)[i]) + ' - '
        season += str(list(HOLIDAY_NAME)[i]).capitalize() + '\n'
    return season


# Ответ от бота
def bot_message(
    user_id, message, vk_comunity, keyboard
):
    vk_comunity.method(
        'messages.send',
        {
            'user_id': user_id,
            'message': message,
            'keyboard': keyboard.get_keyboard(),
            'random_id': randint(1, 100000000)
        }
    )


# Создание клавы
def get_keyboard():
    keyboard = VkKeyboard(one_time=False)

    # Добавляем кнопки
    keyboard.add_button('Описание', color=VkKeyboardColor.DEFAULT)
    keyboard.add_line()

    keyboard.add_button('Все праздники зимы', color=VkKeyboardColor.DEFAULT)
    keyboard.add_line()

    keyboard.add_button('Все праздники весны', color=VkKeyboardColor.DEFAULT)
    keyboard.add_line()

    keyboard.add_button('Все праздники лета', color=VkKeyboardColor.DEFAULT)
    keyboard.add_line()

    keyboard.add_button('Все праздники осени', color=VkKeyboardColor.DEFAULT)

    return keyboard


# Запуск бота
def bot_launch(longpoll, vk_comunity, keyboard):
    print('Бот запущен \U0001F916')
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                # Объект бота
                bot = VkBot(event.user_id)

                print('\nНовое сообщение \U0001F4EC')
                print(f'ID: {event.user_id} \U0001F194')
                print(f'Имя: {bot._get_user_name(event.user_id)} \U0001F974')
                print(f'Текст: {event.text} \U0001F4DD')

                # Бот отвечает
                bot_message(event.user_id, bot.new_message(event.text),
                            vk_comunity, keyboard
                            )


def main():
    # Авторизация сообщества
    vk_comunity = vk_api.VkApi(token=CONST_TOKEN)

    # Работа с сообщениями
    longpoll = VkLongPoll(vk_comunity)

    # Получаем клаву
    keyboard = get_keyboard()

    # Запускаем бота
    bot_launch(longpoll, vk_comunity, keyboard)


if __name__ == '__main__':
    main()

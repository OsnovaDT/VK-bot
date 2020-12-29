import vk_api

from requests import get
from config import (
    CONST_DESCRIPTION, ALL_WINTER_HOLIDAYS, ALL_SPRING_HOLIDAYS,
    ALL_SUMMER_HOLIDAYS, ALL_AUTUMN_HOLIDAYS, HOLIDAY_DAY,
    CONST_SEPARATOR, HOLIDAY_NAME
)
from re import findall
from bs4 import BeautifulSoup


class VkBot:
    def __init__(self, user_id):
        self._USER_ID = user_id

    @staticmethod
    def _clean_all_tags(string_line):
        result, not_skip = '', True
        for i in list(string_line):
            if not_skip:
                if i == '<':
                    not_skip = False
                else:
                    result += i
            else:
                if i == '>':
                    not_skip = True
        return result

    def _get_user_name(self, user_id):
        request = get('https://vk.com/id' + str(user_id))
        bs = BeautifulSoup(request.text, 'html.parser')
        user_name = self._clean_all_tags(bs.findAll('title')[0])

        return user_name.split()[0] + ' ' + user_name.split()[1]

    def new_message(self, message):
        message = message.lower()
        # Описание
        if message == 'описание':
            return CONST_DESCRIPTION

        # Все праздники зимы
        elif message == 'все праздники зимы':
            return ALL_WINTER_HOLIDAYS

        # Все праздники весны
        elif message == 'все праздники весны':
            return ALL_SPRING_HOLIDAYS

        # Все праздники лета
        elif message == 'все праздники лета':
            return ALL_SUMMER_HOLIDAYS

        # Все праздники осени
        elif message == 'все праздники осени':
            return ALL_AUTUMN_HOLIDAYS

        # Привет
        elif findall('^прив', message):
            return f'Привет, {self._get_user_name(self._USER_ID)} \U0001F44B'

        # Дата праздника
        elif findall(r'\d+\s+[а-я]+', message):
            message = CONST_SEPARATOR.join(findall(r'\d+|[а-я]+', message))
            return HOLIDAY_DAY.get(message, 'Нет праздника в этот день \U0001F97A')

        else:
            message = CONST_SEPARATOR.join(findall(r'[а-я]+', message))
            return HOLIDAY_NAME.get(message, 'Нет такого праздника \U0001F928')

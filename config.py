from pandas import read_html
from decouple import config

from main_vk_bot import set_season_holidays


CONST_TOKEN = config('CONST_TOKEN')

CONST_TABLES = read_html('https://infotables.rustrany-i-goroda/17-kalendari/\
174-prazdniki-i-professionalnye-prazdnichnye-mezhdunarodnye-dni-tablitsa')[0]

CONST_EMOJIS = {
    '1 января': '\U0001F384',
    '7 января': '\U0001F385',
    '19 января': '\U0001F91E',
    '25 января': '\U0001F393',
    '26 январь': '\U0001F6C3',
    '28 января': '\U0001F4A3',
    '30 января': '\U0001F48A',
    '8 февраля': '\U0001F52C',
    '11 февраля': '\U0001F984',
    '14 февраля': '\U0001F48F',
    '17 февраля': '\U0001F609',
    '18 февраля': '\U0001F46E',
    '3 марта': '\U0001F58A',
    '8 марта': '\U0001F490',
    '1 апреля': '\U0001F923',
    '9 мая': '\U0001F3F3',
    '1 июня': '\U0001F476',
    '1 сентября': '\U0001F4DA',
    '31 октября': '\U0001F5A4 \U0001F30A',
    '17 ноября': '\U0001F393',
    '10 ноября': '\U0001F37B',
    '28 декабря': '\U0001F4F9'
}

CONST_DESCRIPTION = '''Бот "День праздника" \U0001F916
позволяет получить дату \U0001F4C6
праздника по его названию,
или наоборот, название 
праздника по его дате.

Для получения названия
праздника, введите дату
в таком формате:
ЧИСЛО МЕСЯЦ
Например: 1 сентября

Для получения даты
праздника введите 
название праздника
в любом регистре
Например: День знаний

Также, можно получить
даты и названия праздников
для каждого времени года
для этого введите данные
в таком формате:
Все праздники ВРЕМЯ_ГОДА

Для того чтобы 
поздороваться с ботом
введите слово,
начинающееся с 'прив'.
'''

CONST_SEPARATOR = ' '

CONST_DEFAULT_EMOJI = ' \U0001F5D3'


# Таблица дней
HOLIDAY_DAY = {}
for i in range(1, len(CONST_TABLES)):
    holiday_emoji = CONST_EMOJIS.get(CONST_TABLES[0][i], CONST_DEFAULT_EMOJI)
    HOLIDAY_DAY[CONST_TABLES[0][i]] = {
        CONST_TABLES[1][i] + ' ' + holiday_emoji}

# Таблица названий
HOLIDAY_NAME = {}
for i in range(1, len(CONST_TABLES)):
    HOLIDAY_NAME[CONST_TABLES[1][i].lower()] = \
        {CONST_TABLES[0][i] + CONST_DEFAULT_EMOJI}

# Праздники по сезонам
ALL_WINTER_HOLIDAYS = set_season_holidays(-16, 24)
ALL_SPRING_HOLIDAYS = set_season_holidays(24, 80)
ALL_SUMMER_HOLIDAYS = set_season_holidays(80, 122)
ALL_AUTUMN_HOLIDAYS = set_season_holidays(122, 179)

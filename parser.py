from bs4 import BeautifulSoup
import requests
import sqlite3
import traceback
import sys

# r = requests.get('https://shikimori.one/animes/37984-kumo-desu-ga-nani-ka', headers={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'})
# print(r.text)
# soup = BeautifulSoup(r.text, 'html.parser')
# result = soup.find_all("div", class_="b-enty-info")
# print(result)

result = ['<div class="b-entry-info"><div class="line-container"> <div class="line"> <div class="key">Тип:</div> <div class="value">TV Сериал</div> </div> </div><div class="line-container"> <div class="line"> <div class="key">Эпизоды:</div> <div class="value">12 / 24</div> </div> </div><div class="line-container"> <div class="line"> <div class="key">Следующий эпизод:</div> <div class="value">9 апр. 15:30</div> </div> </div><div class="line-container"> <div class="line"> <div class="key">Длительность эпизода:</div> <div class="value"><span>23 мин.</span></div> </div> </div><div class="line-container"> <div class="line"> <div class="key">Статус:</div> <div class="value"><span class="b-anime_status_tag ongoing" data-text="онгоинг"></span> с 8 янв. 2021 г.</div> </div> </div><div class="line-container"> <div class="line"> <div class="key">Жанры:</div> <div class="value"><span class="b-tag" data-delay="150" data-href="https://shikimori.one/moderations/genres/2-Adventure/tooltip" itemprop="genre"><span class="genre-en">Adventure</span><span class="genre-ru">Приключения</span></span><span class="b-tag bubbled" data-delay="150" data-href="https://shikimori.one/moderations/genres/7-Mystery/tooltip" itemprop="genre"><span class="genre-en">Mystery</span><span class="genre-ru">Детектив</span></span><span class="b-tag bubbled" data-delay="150" data-href="https://shikimori.one/moderations/genres/4-Comedy/tooltip" itemprop="genre"><span class="genre-en">Comedy</span><span class="genre-ru">Комедия</span></span><span class="b-tag bubbled" data-delay="150" data-href="https://shikimori.one/moderations/genres/10-Fantasy/tooltip" itemprop="genre"><span class="genre-en">Fantasy</span><span class="genre-ru">Фэнтези</span></span></div> </div> </div><div class="line-container"> <div class="line"> <div class="key">Рейтинг:</div> <div class="value"><span class="b-tooltipped dotted mobile unprocessed" data-direction="right" title="PG-13 - Детям до 13 лет просмотр не желателен">PG-13</span></div> </div> </div><div class="line-container"> <div class="line"> <div class="key">Лицензировано:</div> <div class="value">Crunchyroll</div> </div> </div><div class="line-container"> <div class="line"> <div class="key">Лицензировано в РФ под названием:</div> <div class="value"><span itemprop="alternativeHeadline">Да, я паук, и что?</span></div> </div> </div><div class="line-container"> <div class="line"> <div class="key">Альтернативные названия:</div> <div class="value"><span class="other-names to-process" data-clickloaded-url="https://shikimori.one/animes/37984-kumo-desu-ga-nani-ka/other_names" data-dynamic="clickloaded"><span>···</span></span></div> </div> </div><div class="additional-links"><div class="line-container"><div class="key">У аниме:</div><span class="linkeable" data-href="https://shikimori.one/animes/37984-kumo-desu-ga-nani-ka/summaries">4 отзыва</span><span class="linkeable" data-href="https://shikimori.one/forum/animanga/anime-37984-kumo-desu-ga-nani-ka/257218-obsuzhdenie-anime">1190 комментариев</span></div></div><div class="additional-links"><div class="line-container"><span class="linkeable" data-href="https://shikimori.one/animes/37984-kumo-desu-ga-nani-ka/art">Арт с имиджборд</span><span class="linkeable" data-href="https://shikimori.one/animes/37984-kumo-desu-ga-nani-ka/coub">Coub</span></div></div></div>',]

for i in result:
    # print(i)
    soup2 = BeautifulSoup(str(i), "html.parser")
    # print(soup2.prettify())
    block = soup2.find_all("div", class_="line-container")
    # print(block)
    ep_count = block[1].find_all("div", class_="value")
    next_ep = block[2].find_all("div", class_="value")
    ep_count_val = str(ep_count[0].get_text())
    next_ep_val = str(next_ep[0].get_text())

try:
    sqlite_connection = sqlite3.connect('db.sqlite3')
    cursor = sqlite_connection.cursor()
    print("База данных  успешно подключена")

    sqlite_insert_query = "UPDATE app_title SET episodes = '%s', release_date = '%s' WHERE name = 'toradora'" % (ep_count_val, next_ep_val)
    print(sqlite_insert_query)
    count = cursor.execute(sqlite_insert_query)
    sqlite_connection.commit()
    print("Запись успешно вставлена ​​в таблицу db.sqlite3", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Не удалось вставить данные в таблицу sqlite")
    print("Класс исключения", error.__class__)
    print("Исключение", error.args)
    print("Печать подробноcтей исключения SQLite: ")
    exc_type, exc_value, exc_tb = sys.exc_info()
    print(traceback.format_exception(exc_type, exc_value, exc_tb))
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
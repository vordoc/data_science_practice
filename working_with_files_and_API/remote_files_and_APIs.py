from pprint import pprint
import requests
import urllib3
import json
from news_api_org__api_key import NEWS_ORG_API_KEY

"""Доступ к удаленным файлам и API

Некоторые сторонние библиотеки Python, включая urllib3 и Requests, позволяют получить данные из удаленного файла,
доступного по URL. Библиотеки также можно использовать для отправки запросов к HTTP API (API, использующим
HTTP в качестве протокола передачи данных).

Многие из них возвращают запрашиваемые данные в формате JSON. И urllib3, и Requests
формируют пользовательские HTTP-запросы на основе введенной информации.
HTTP (HyperText Transfer Protocol — протокол передачи гипертекста), клиент-серверный протокол, составляющий основу
обмена данными в интернете, структурирован как серия запросов и ответов.
HTTP-сообщение, посылаемое клиентом, — это запрос (request), а сообщение, возвращаемое сервером, — ответ (response).
Скрипт, выступающий в роли клиента, получает запрашиваемые данные в виде документа JSON или XML.

Как работают HTTP-запросы
Существует несколько типов HTTP-запросов. Наиболее популярные из них — GET, POST, PUT и DELETE.
Они также известны как методы HTTP-запросов или просто HTTP-команды (HTTP command / HTTP verb). Команда HTTP в любом
HTTP-запросе определяет действие, которое необходимо выполнить с указанным ресурсом. Например, GET-запрос получает
данные из ресурса, а POST-запрос отправляет данные в место назначения.

HTTP-запрос включает цель запроса (target) — обычно это URL-адрес, а также
заголовки (headers), которые представляют собой поля, передающие вместе с запросом дополнительную информацию.
В некоторых запросах также есть тело. Доступ к удаленным файлам и API 97 (body), которое содержит фактические данные
запроса, например отправку формы. POST-запросы обычно имеют тело, а GET-запросы — нет.

В дальнейшем мы подробно обсудим библиотеку Requests. А пока обратите внимание, 
что она избавляет от необходимости задавать заголовки запроса вручную. 
Requests скрыто устанавливает значения по умолчанию, автоматически генерируя полностью отформатированный 
HTTP-запрос от вашего имени всего несколькими строками кода."""

PARAMS = {'bibkeys': 'ISBN:1718500521', 'format': 'json'}
info = requests.get('http://openlibrary.org/api/books', params=PARAMS)
print(info)

print("\n--------------------------------------------------------------\n")


"""Библиотека urllib3
urllib3 — это библиотека для работы с URL. Она позволяет получать доступ к URL-ресурсам, таким как HTTP API, 
веб-сайты и файлы, и управлять ими. 
Эта библиотека предназначена для эффективной обработки HTTP-запросов с помощью потокобезопасного пула соединений, 
что минимизирует количество необходимых серверных ресурсов.
По сравнению с библиотекой Requests, которую мы рассмотрим далее, urllib3 требует больше ручных операций, 
однако она предоставляет больше прямого контроля над создаваемыми запросами, что может быть полезно при настройке 
поведения пула или расшифровке HTTP-ответов.

urllib3 также можно использовать для выполнения запросов к HTTP API. 
В примере ниже мы делаем запрос к News API1, который выполняет поиск наиболее 
релевантных запросу статей из множества новостных источников.

Мы передаем поисковую фразу в качестве параметра q в URL-адресе запроса. 
Ключ АПИ передаем в параметр apiKey. 
Полный список поддерживаемых параметров можно найти в документации News API. 

Атрибут data объекта HTTPResponse, возвращаемого функцией request(), — документ JSON в виде объекта bytes. 
Мы преобразовываем его в строку, которую затем передаем методу json.loads() для преобразования в словарь.
Далее нам остается распарсить полученный словарь"""


http = urllib3.PoolManager()
r = http.request('GET', f'https://newsapi.org/v2/everything?q=tesla&from=2023-12-11&sortBy='
						f'publishedAt&pageSize=5&apiKey={NEWS_ORG_API_KEY}')
# print(r)
articles = json.loads(r.data.decode('utf-8'))
# pprint(articles)
for article in articles['articles']:
	print(article['title'])
	print(article['publishedAt'])
	print(article['url'])
	print('---------------------------------------------------')



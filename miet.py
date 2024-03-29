import requests
import json
from bs4 import BeautifulSoup as bs

headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
        }

urls = ['https://miet.ru/people/192',
       'https://miet.ru/people/193',
       'https://miet.ru/people/194',
       'https://miet.ru/people/195',
       'https://miet.ru/people/196',
       'https://miet.ru/people/197',
       'https://miet.ru/people/198',
       'https://miet.ru/people/199',
       'https://miet.ru/people/200',
       'https://miet.ru/people/202',
       'https://miet.ru/people/203',
       'https://miet.ru/people/204',
       'https://miet.ru/people/205',
       'https://miet.ru/people/206',
       'https://miet.ru/people/207',
       'https://miet.ru/people/208',
       'https://miet.ru/people/209',
       'https://miet.ru/people/210',
       'https://miet.ru/people/211',
       'https://miet.ru/people/212',
       'https://miet.ru/people/213',
       'https://miet.ru/people/214',
       'https://miet.ru/people/215',
       'https://miet.ru/people/216',
       'https://miet.ru/people/217',
       'https://miet.ru/people/222',
       'https://miet.ru/people/223',
		]
teachers = {}
#Парсинг сайта и создание словаря с преподавателями
def miet_parser(url):
	session = requests.session()
	request = session.get(url, headers=headers)
	if request.status_code == 200:
		soup = bs(request.content, 'html.parser')
		divs = soup.find_all('div', attrs = {'class': 'people-list__item'})
		for div in divs:
			name = div.find('a', attrs = {'class': 'people-list__item-name'}).text
			teacher = {'name': name,
			'post': div.find('span', attrs = {'class': 'people-list__item-post'}).text}
			email = div.find('span', attrs = {'class': 'people-list__item-email'})
			if email:
				#text_email = email.textddd
				#text_email.split()
				teacher.update({'email': email.text})
			name_split = name.split()
			short_name = name#f'{name_split[0]} {name_split[1][0]}.{name_split[2][0]}.'
			teachers.update({short_name: teacher.copy()})
			teacher.clear()
#Запись словаря в Json
def dict_to_json():
	with open("teachers.json", "w", encoding='utf-8') as write_file:
		write_file.write(json.dumps(teachers, ensure_ascii=False))
	print('Secsess')
#Вызов функций
for url in urls:
	miet_parser(url)
dict_to_json()


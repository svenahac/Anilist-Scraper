import requests
from bs4 import BeautifulSoup as bs

def stats(user):
    url = 'https://anilist.co/user/'
    #user = input('Input Anilist Username: ')
    results = requests.get(url + user)
    src = results.content
    soup = bs(src, 'lxml')

    stats = soup.find_all('div', class_='stat')
    for i in stats:
        name = i.find('div', class_ = 'label').text
        value = i.find('div', class_ = 'value').text
        print(f'{name}: {value}')
    if stats == []:
        print("Username doesn't exist")





import requests
from bs4 import BeautifulSoup as bs

def watchlist(user):
    url = 'https://anilist.co/user/'
    results = requests.get(url + user + '/animelist')
    #print(results.status_code)

    src = results.content
    soup = bs(src, 'lxml')

    watchlist = soup.find_all('div', class_ = 'entry row')
    if watchlist == []:
        print ('Username does not exist')
    else:
        for i in watchlist:
            status = i.find('div', class_ = 'status').text
            if status == 'Current':
                status = 'Watching'
            else:
                status = status
            anime_name = i.find('a').text.replace('\n','')
            score = i.find('div', class_ = 'score').text.replace('\n','')
            if score == '':
                score = 'Unscored'
            else:
                score = score
            progress = (i.find('div', class_ = 'progress').text.replace('\n','').replace('+', ''))
            form = i.find('div', class_ = 'format').text.replace('\n','')
            print(f'Anime: {anime_name} \n Status: {status} \n Score: {score} \n Progress: {progress} \n Format: {form}')
            print('------------------------------------------------')

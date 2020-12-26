import requests
from bs4 import BeautifulSoup as bs
import stats
import watchlist


user= input('Input Anilist Username: ')
action = int(input('Enter 1 for stats or 2 for watchlist: '))
if action == 1:
    stats.stats(user)
elif action == 2:
    watchlist.watchlist(user)

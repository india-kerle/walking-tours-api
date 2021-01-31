import urllib.parse
import requests
from bs4 import BeautifulSoup, SoupStrainer
from collections import defaultdict
import datetime
from datetime import timedelta

def tours_between_two_dates(start, end, step = timedelta(days = 1)):
    
    date_format = "%Y-%m-%d"
    
    st = datetime.datetime.strptime(start, date_format).date()
    en = datetime.datetime.strptime(end, date_format).date()

    curr = st
    while curr <= en:
        yield curr
        curr += step

def between_two_dates(start, end):
    
    dates = list(tours_between_two_dates(start, end, step = timedelta(days = 1)))
    all_the_dates = [str(j) for j in dates]
    
    return all_the_dates

def get_walk_info(all_the_dates):
    
    base_url = "https://www.walks.com/our-walks/walks-by-date/"

    main = []
    for day in all_the_dates:
        urls = base_url + "?d=" + day
        responses = requests.get(urls)
        soup_strainer = SoupStrainer('div', {"class": "walkrow suspended-walkrow"})
        soups = BeautifulSoup(responses.content, 'html.parser', parse_only = soup_strainer)
        guides = soups.findAll('a', {'class':'guideLink'}, href = True)
        tube = soups.findAll(class_ = "tube")
        description = soups.findAll('div', {'class':'description'})
        time = soups.findAll('div', {'class': 'col-xs-3 time'})


        for index, item in enumerate(soups.findAll('a', {'class':'h4Title'}, href = True)):
            try:
                walks = {}
                walks['tour_date'] = day
                walks['tour_time'] = time[index].text.strip()
                walks['tour_name'] = item.text
                walks['tour_desc_short'] = description[index].p.text.strip()
                walks['meeting_spot'] = tube[index].text
                walks['tour_link'] = item['href']
                walks['guide_name'] = guides[index].text
                walks['guide_link'] = "https://walks.com" + guides[index]['href']
                
                main.append(walks)
            except IndexError:
                continue
    
    return main  

def get_guide_info():
    
    response = requests.get('https://www.walks.com/guides/')
    soup = BeautifulSoup(response.content, 'html.parser')

    guide = []
    for g in soup.findAll("div", {'class': 'collapse-list-item'}):
        guides = {}
        try:
            guides['guide_name'] = g.h4.text
            guides['guide_link']= "https://walks.com/guides/" + g.a['href']
            guides['guide_description'] = g.p.text

            guide.append(guides)

        except AttributeError:
            continue
    
    return guide

def get_tours(start, end):
    all_the_dates = between_two_dates(start, end)
    walks = get_walk_info(all_the_dates)
    
    return walks 

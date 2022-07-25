import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get('https://news.ycombinator.com/')
response2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(response.text, 'html.parser')
soup2 = BeautifulSoup(response2.text, 'html.parser')

# print(soup.find_all('div'))
_links = soup.select('.titlelink')
_links2 = soup2.select('.titlelink')
# votes = soup.select('.score')
_subtext = soup.select('.subtext')
_subtext2 = soup2.select('.subtext')

mega_links = _links + _links2
mega_subtext = _subtext + _subtext2


def sort_stories_by_vote(hn_list):
    return sorted(hn_list, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 80:
                hn.append({
                    'title': title,
                    'link': href,
                    'votes': points
                })
    return sort_stories_by_vote(hn)


pprint.pprint(create_custom_hn(mega_links, mega_subtext))

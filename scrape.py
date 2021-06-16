import requests
from bs4 import BeautifulSoup
import pprint

def sort_hn_by_votes(hn):
  return sorted(hn, key= lambda x:x['points'], reverse=True)

def create_custom_hn(links, subtext):
  hn = []
  for ind, item in enumerate(links):
    title = links[ind].getText()
    href = links[ind].get('href', None)
    vote = subtext[ind].select('.score')
    if len(vote):
      points = int(vote[0].getText().replace(' points', ''))
      if points >= 100:
        hn.append({
          'title': title,
          'link': href,
          'points': points
        })
  return sort_hn_by_votes(hn)

def get_links_and_points(num_pages=1):
  links = []
  subtext = []
  for page in range(1, num_pages + 1):
    res = requests.get(f'https://news.ycombinator.com/news?p={page}')
    soup = BeautifulSoup(res.text, 'html.parser')
    links.extend(soup.select('.storylink'))
    subtext.extend(soup.select('.subtext'))
  return create_custom_hn(links, subtext)


pprint.pprint(get_links_and_points(3))


import requests
from bs4 import BeautifulSoup
from django.conf import settings


def fetch_open_graph_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    og_data = {
        'title': soup.find('meta', property='og:title'),
        'description': soup.find('meta', property='og:description'),
        'image': soup.find('meta', property='og:image'),
        'type': soup.find('meta', property='og:type')
    }

    og_data = {key: (tag['content'] if tag else None) for key, tag in og_data.items()}

    if not og_data['title']:
        og_data['title'] = soup.find('title').text if soup.find('title') else 'No title'
    if not og_data['description']:
        og_data['description'] = soup.find('meta', attrs={'name': 'description'})['content'] if soup.find('meta',
                                                                                                          attrs={
                                                                                                              'name': 'description'}) else 'No description'
    if not og_data['image']:
        og_data['image'] = f'{settings.STATIC_URL}api/img/og.png'
    if not og_data['type']:
        og_data['type'] = 'website'
    return og_data

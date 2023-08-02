import requests
from bs4 import BeautifulSoup


def find_links_in_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the request was not successful
        soup = BeautifulSoup(response.content, 'html.parser')

        links = [a.get('href') for a in soup.find_all('a', href=True)]
        return {url: links}

    except requests.exceptions.RequestException as e:
        return {url: {"error": str(e)}}
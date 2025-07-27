import re
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

def extract_links(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    links = set()
    for tag in soup.find_all('a', href=True):
        href = tag['href'].strip()
        full_url = urljoin(base_url, href)
        if urlparse(full_url).scheme in ('http', 'https'):
            links.add(full_url)
    return list(links)

def skim_page_for_js(html):
    return bool(re.search(r'<script|javascript:', html, re.I))

# ONIONS, HAVE... LAYERS!

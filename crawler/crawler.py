from bs4 import BeautifulSoup
import urllib.request
import re
import hashlib
import os
import time
import random

PAGES_DIR = 'pages/'


def crawl(seed, url_limit=10):
    """
    Web crawler that will download HTML content from pages it visits.

    Args:
        - seed: Starting point for the crawler
        - url_limit: Max amount of pages the crawler will visit (defaults to 10)
    """
    mst_pattern = re.compile('\.mst\.edu')  # Only crawl MST pages
    terminal_four = re.compile('tsxapp\.mst\.edu\/*') # Site manager page that appears frequently

    frontier = [seed]
    visited = set()

    while len(visited) < url_limit and len(frontier) > 0:
        current_url = frontier.pop()

        # Ignore this site manager page
        if terminal_four.search(current_url) != None:
            print('found a terminal four site! skipping...', current_url)
            continue

        try:
            response = urllib.request.urlopen(current_url)
        except urllib.request.HTTPError:
            print('could not get content for', current_url)
            continue

        # Check that the content type is HTML
        content_type = response.info().get('Content-Type')
        if not content_type.startswith('text/html'):
            print('skipping', content_type)
            continue

        content = response.read()

        soup = BeautifulSoup(content, features='html.parser')
        filename = PAGES_DIR + hashlib.md5(current_url.encode()).hexdigest() + '.html'

        visited.add(current_url)

        with open(filename, 'w') as f:
            # Remove all javascript and css
            for tag in soup(["script", "style"]):
                tag.decompose()

            print('-------------------------------------------------')
            print('{:15} ==> {:10}'.format('url', current_url))
            print('{:15} ==> {:10}'.format('title', soup.title.string))
            print('{:15} ==> {:10}'.format('filename', filename))
            print('-------------------------------------------------')
            f.write(soup.prettify())

        # Get all mst domain links on the page
        mst_tags = [str(a.get('href')) for a in soup.find_all('a') if mst_pattern.search(str(a.get('href'))) != None]

        # Get all discovered and unique links
        discovered = {link for link in mst_tags if link not in visited}

        # Add the discovered links to the pages left to visit
        frontier.extend(discovered)

        time.sleep(random.random())


if __name__ == "__main__":
    seed = 'https://www.mst.edu/'

    # Make a 'pages' directory if it doesn't already exist
    if not os.path.isdir(PAGES_DIR):
        os.mkdir(PAGES_DIR)

    crawl(seed)

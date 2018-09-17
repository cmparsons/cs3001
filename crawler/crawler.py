from bs4 import BeautifulSoup
import urllib.request
import re
import hashlib
import os

PAGES_DIR = 'crawler/pages/'

def crawl(seed, url_limit=10):
    mst_pattern = re.compile('\.mst\.edu')

    frontier = [seed]
    visited = set()
    i = 0

    while i < url_limit and len(frontier) > 0:
        current_url = frontier.pop()

        if current_url in visited:
            break
        else:
            visited.add(current_url)
            i += 1

        content = urllib.request.urlopen(current_url).read()
        soup = BeautifulSoup(content, features='html.parser')
        filename = PAGES_DIR + hashlib.md5(current_url.encode()).hexdigest() + '.html'

        with open(filename, 'w') as f:
            # Remove all javascript and css
            for tag in soup(["script", "style"]):
                tag.decompose()

            print('Saving url: {} title: {} to file: {}'.format(current_url, soup.title.string, filename))
            f.write(soup.prettify())

        # Get all mst domain links on the page
        mst_tags = [str(a.get('href')) for a in soup.find_all('a') if mst_pattern.search(str(a.get('href'))) != None]

        print('Current:', current_url)
        for link in mst_tags:
            if link not in visited:
                print('\t', link)
                frontier.append(link)


if __name__ == "__main__":
    seed = 'http://www.mst.edu/'

    if not os.path.isdir(PAGES_DIR):
        os.mkdir(PAGES_DIR)

    crawl(seed)

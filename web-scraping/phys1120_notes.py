'''
Install the following dependencies
>>> pip install requests
>>> pip install beautifulsoup4
'''

import requests
import os
import urlparse

from bs4 import BeautifulSoup

def download_pdf(url, downloadpath):
    req = requests.get(url)
    bs = BeautifulSoup(req.text, 'html.parser')
    links = bs.findAll('a', href=True)
    if len(links) == 0:
        print "No pdf links found"
        return

    files = 0
    for link in links:
        if link['href'][-4:] == '.pdf':
            files += 1
            pdf = requests.get(urlparse.urljoin(url, link['href']))
            f = open(os.path.join(downloadpath, link.text + '.pdf'), 'wb')
            f.write(pdf.content)
            f.close()

    print str(files) + " files were downloaded!"
    return

if __name__ == "__main__":
    url = 'http://www.colorado.edu/physics/phys1120/phys1120_sp17/LectureNotes1120/lectureIndex.html'
    path = " " #Your download path goes here
    download_pdf(url, path)
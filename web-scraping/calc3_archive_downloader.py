'''
Install the following dependencies
>>> pip install requests
>>> pip install beautifulsoup4

Maintain the following folder structure within the download path to prevent errors
> downloadpath
    > Fall 2013
    > Fall 2014
    > Fall 2015
    > Spring 2013
    > Spring 2014
    > Spring 2015
    > Spring 2016
    > Summer 2013
    > Summer 2014
    > Summer 2015
    > Summer 2016
    ...
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
        print("No pdf links found")
        return

    files = 0

    for link in links:
        if link['href'][-4:] == '.pdf':
            files += 1
            pdf = requests.get(urlparse.urljoin(url, link['href']))
            #Sort them into folders
            if 'fall2015' in link['href']:
                directory = 'Fall 2015'
                if not os.path.exists(directory):
                    os.makedirs(directory)
                f = open(os.path.join(downloadpath, directory, link.text+'.pdf'), 'wb')
                f.write(pdf.content)
                f.close()
            elif 'spring2015' in link['href']:
                directory = 'Spring 2015'
                if not os.path.exists(directory):
                    os.makedirs(directory)
                f = open(os.path.join(downloadpath, directory, link.text+'.pdf'), 'wb')
                f.write(pdf.content)
                f.close()
            elif 'summer2015' in link['href']:
                directory = 'Summer 2015'
                if not os.path.exists(directory):
                    os.makedirs(directory)
                f = open(os.path.join(downloadpath, directory, link.text+'.pdf'), 'wb')
                f.write(pdf.content)
                f.close()
            elif 'fall2014' in link['href']:
                directory = 'Fall 2014'
                if not os.path.exists(directory):
                    os.makedirs(directory)
                f = open(os.path.join(downloadpath, directory, link.text+'.pdf'), 'wb')
                f.write(pdf.content)
                f.close()
            elif 'spring2014' in link['href']:
                directory = 'Spring 2014'
                if not os.path.exists(directory):
                    os.makedirs(directory)
                f = open(os.path.join(downloadpath, directory, link.text+'.pdf'), 'wb')
                f.write(pdf.content)
                f.close()
            elif 'summer2014' in link['href']:
                directory = 'Summer 2014'
                if not os.path.exists(directory):
                    os.makedirs(directory)
                f = open(os.path.join(downloadpath, directory, link.text+'.pdf'), 'wb')
                f.write(pdf.content)
                f.close()
            elif 'fall2013' in link['href']:
                directory = 'Fall 2013'
                if not os.path.exists(directory):
                    os.makedirs(directory)
                f = open(os.path.join(downloadpath, directory, link.text+'.pdf'), 'wb')
                f.write(pdf.content)
                f.close()
            elif 'spring2013' in link['href']:
                directory = 'Spring 2013'
                if not os.path.exists(directory):
                    os.makedirs(directory)
                f = open(os.path.join(downloadpath, directory, link.text+'.pdf'), 'wb')
                f.write(pdf.content)
                f.close()
            elif 'summer2013' in link['href']:
                directory = 'Summer 2013'
                if not os.path.exists(directory):
                    os.makedirs(directory)
                f = open(os.path.join(downloadpath, directory, link.text+'.pdf'), 'wb')
                f.write(pdf.content)
                f.close()

    print(str(files) + " files were downloaded!")
    return

if __name__ == "__main__":
    url = 'http://www.colorado.edu/amath/academics/exam-archives/appm-2350-exam-archive'
    path = " " #Your download path goes here
    download_pdf(url, path)

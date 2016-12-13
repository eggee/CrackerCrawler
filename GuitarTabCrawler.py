__author__ = 'Tim Eggenberger'

import requests
import urllib2
import os
from bs4 import BeautifulSoup
def guitar_tab_crawler():
    main_url = 'http://www.the-van.co.uk/songs/index.php?artist=Cracker'
    main_source_code = requests.get(main_url)
    main_plain_text = main_source_code.text
    main_soup = BeautifulSoup(main_plain_text)
    #find all the links from the given main-page
    for link in main_soup.findAll('a'):
        song_id = link.get('href')
        if "item_id" in song_id:
            song_url = "http://www.the-van.co.uk/songs/index.php%s&chord=yes" % song_id
            title = link.contents[0]
            #replace any illegal filename characters that may be in the title
            #this will be used to create the new text file name.
            song_title = title.replace('?',"")
            print(song_title)
            print(song_id)
            print(song_url)
            #
            song_source_code = urllib2.urlopen(song_url)
            song_soup = BeautifulSoup(song_source_code.read())
            song_lyrics = song_soup.get_text().encode("windows-1252")
            #removes all blank lines from the string
            song_lyrics = os.linesep.join([s for s in song_lyrics.splitlines() if s])
            #print(song_lyrics)
            #write the song lyrics each to it's own filename
            filename = ('C:/CrackerTabs/%s.txt' % song_title)
            f = open(filename, 'wb')
            f.write(song_lyrics)
            f.close()
#call the def
guitar_tab_crawler()

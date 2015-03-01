__author__ = 'aron'
from ID3 import *
import requests
import urllib
import pandas as pd
import numpy as np
import sys
import time
import os
from difflib import SequenceMatcher as sm
from mutagen.mp3 import MP3
import ipdb

class DownloadSC():
    jsons = list()
    df = None
    download_progress = 0
    likes = False
    current_time = time.time()

    def __init__(self):
        current_dir = os.getcwd()
        os.chdir("c:/Users/aron/Music/aphex online/")
        self.json_list()
        self.create_df()
        self.whichFiles()
        self.downloadSongs()
        os.chdir(current_dir)

    def json_list(self):
        offset = 0
        l = 50
        while l >= 50:
            api = "http://api.soundcloud.com/users/122922135/tracks.json?client_id=YOUR_CLIENT_ID&offset=" + str(
                offset * 50)
            r = requests.get(api)
            self.jsons += (r.json())
            l = len(r.json())
            offset += 1

    def create_df(self):
        self.df = pd.DataFrame(np.array([[x['download_url'] for x in self.jsons], [x['title'] for x in self.jsons]]).transpose())
        self.df.columns = ['url', 'title']
        self.df['download_flag'] = False
        #self.df = self.df.iloc[1:4, :]


    def whichFiles(self):
        for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
            for fn in filenames:
                for title in self.df['title']:
                    try:
                        if sm(None, fn, title + ".mp3").ratio() > 0.7:
                            #print self.df[self.df['title'] == title]['download_flag']
                            i = d.df[d.df['title'] == 'X - Rays'].index.values[0]
                            self.df['download_flag'].iloc[i] = True
                    except Exception,e:
                        print(e)
                        print(title)

    def downloadSongs(self):

        done = False
        for url, title, flag in zip(self.df['url'], self.df['title'], self.df['url']):
            if not done and flag:
                try:
                    filename = "{0}.mp3".format(title)
                    sys.stdout.write("\nDownloading: {0}\n".format(filename))
                    if not os.path.isfile(filename):
                        print url+"client_id=YOUR_CLIENT_ID"
                        filename, headers = urllib.urlretrieve(url=url+"?client_id=YOUR_CLIENT_ID", filename=filename, reporthook=self.report)
                        # self.addID3(title, artist)
                        # reset download progress to report multiple track download progress correctly
                        self.download_progress = 0
                    elif self.likes:
                        print "File Exists"
                        done = True
                    else:
                        print "File Exists"
                except Exception, e:
                    print str(e)
                    print "ERROR: Author has not set song to streamable, so it cannot be downloaded"


    def report(self, block_no, block_size, file_size):
        self.download_progress += block_size
        if int(self.download_progress / 1024 * 8) > 1000:
            speed = "{0} Mbps".format(
                round((self.download_progress / 1024 / 1024 * 8) / (time.time() - self.current_time), 2))
        else:
            speed = "{0} Kbps".format(round((self.download_progress / 1024 * 8) / (time.time() - self.current_time), 2))
        rProgress = round(self.download_progress / 1024.00 / 1024.00, 2)
        rFile = round(file_size / 1024.00 / 1024.00, 2)
        percent = round(100 * float(self.download_progress) / float(file_size))
        sys.stdout.write("\r {3} ({0:.2f}/{1:.2f}MB): {2:.2f}%".format(rProgress, rFile, percent, speed))
    sys.stdout.flush()


#d = DownloadSC()


class performID3:

    def __init__(self):
        current_dir = os.getcwd()
        os.chdir("c:/Users/aron/Music/aphex online/")
        self.list_id3()
        #self.removeTags()
        os.chdir(current_dir)

    def list_id3(self):
        for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
            print filenames
            for fn in filenames:
                try:
                    id = ID3(dirpath + "/" + fn)
                    id.artits = "Aphex"
                    id.title = fn[0:-4]
                    id.album = 'sc'
                    id.artist = 'Aphex'
                    id.write()
                    #if not id.title:
                    #    print "The file " + fn + " has no title."
                    #    print id.title

                    #print(fn +  " " + id.artist + " " + id.title)
                except Exception,e:
                    print("Error: " + fn + str(e))
                    #ipdb.set_trace()

    def removeTags(self):
        for fn in os.listdir("c:/Users/aron/Music/aphex online/"):
            fname = os.path.join("c:/Users/aron/Music/aphex online/", fn)
            if fname.lower().endswith('.mp3'):
                print fn,
                mp3 = MP3(fname)
                #mp3.delete()
                try:
                    mp3.delete()
                    mp3.save()
                    print 'ok!'
                except:
                    print 'no ID3 tag'
    print 'Done'

p = performID3()

df = pd.DataFrame()
df.merge()
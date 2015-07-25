__author__ = 'mattias'

from flask import Flask
from flask import render_template
import feedparser
import urllib, collections, hmac, binascii, time, random, string
from hashlib import sha1

app = Flask(__name__)

app.config.setdefault('TWEEPY_CONSUMER_KEY', 'aRahVNAuCVdWy5PGFjMoAIWui')
app.config.setdefault('TWEEPY_CONSUMER_SECRET', 'fABUmGW1uV4pnlgTpwSx8KAxQdbVH6fz2le4dEW4e9wlnxmP2b')
app.config.setdefault('TWEEPY_ACCESS_TOKEN_KEY', '2834176217-coE5CGfxIdniddoou1HOBcG3r4KVdVG2UzJQStS')
app.config.setdefault('TWEEPY_ACCESS_TOKEN_SECRET', '3tfg6G4clDY42ie6wYekxf77xHGKCZjmWtUzIEqRTHqoW')

@app.route('/')
def index():
    ##### RSS Feed Urls:
    CSGO_URL = ['http://blog.counter-strike.net/index.php/feed/']

    DOTA_URL = ['http://blog.dota2.com/feed/']

    TF2_URL = ['http://www.teamfortress.com/rss.xml']

    SOURCEFILM_URL = ['http://www.sourcefilmmaker.com/rss.xml']

    ##### CSGO Feed
    csgo_entries = []
    for url in CSGO_URL:
        csgo_entries.extend(feedparser.parse(url).entries)

    csgo_entries_sorted = sorted(
        csgo_entries,
        key=lambda e: e.published_parsed,
        reverse=True)

##### ===>
##### ===>

    return render_template('index.html', entries=csgo_entries_sorted)

if __name__ == '__main__':
    app.run()

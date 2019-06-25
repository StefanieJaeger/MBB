import feedparser
import re

import data_manager

token = data_manager.getCredentials("moodle")
feed = None

def updateRSS():
    global feed
    feed = feedparser.parse("https://moodle.bbbaden.ch/rss/file.php/1/" + token + "/blog/user/9999/rss.xml")

def sanitiseHTML(html):
    for line in html:
        cleanr = re.compile('(<\/?(li|ul|p|br) ?\/?>)')
        html = re.sub(cleanr, '', html)

    return html


def getAllEntries():
    updateRSS()
    entries = {}
    for entry in feed.entries:
        entries[entry.published, "title"] = [feed.entries[0].title]
        entries[entry.published, "summary"] = [feed.entries[0].summary]

    print(entries["Mon, 17 Jun 2019 15:44:08 GMT", "title"])

    return entries


def getLastEntry():
    updateRSS()
    entry = {}
    entry["published"] = feed.entries[0].published
    entry["title"] = feed.entries[0].title
    entry["summary"] = sanitiseHTML(feed.entries[0].summary)
    return entry

import os, sys, pdb, json
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from unicodedata import normalize
import requests

def make_json_from_xml(lang, vid_id):
    xml = requests.get('http://video.google.com/timedtext?lang=' + lang + '&v=' + vid_id).text
    soup = BeautifulSoup(xml, 'xml')
    fin_txt = FUCKXML([i for i in soup.children][0])
    return {'json':json.dumps(fin_txt), 'lang':lang}

def FUCKXML(soup):
    out = []
    for child in soup.children:
        out.append({u'ts':child['start'],u'l':BeautifulSoup(child.text, 'lxml').text})
    return out

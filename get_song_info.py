import sys,json,requests,pdb

_, SONG_ID,SONG_TITLE,SONG_ARTIST,GRAPH_ID,SONG_IMG,GOOGLE_API_KEY = sys.argv
caption_candidates = json.loads(requests.get("https://www.googleapis.com/youtube/v3/captions/?part=snippet&videoId=%s&key=%s"%(SONG_ID,GOOGLE_API_KEY)).text)['items']

song_info = {
    'title':SONG_TITLE,
    'artist':SONG_ARTIST,
    'img':SONG_IMG,
    'languages':[str(i['snippet']['language']) for i in caption_candidates]
}

for i in song_info['languages']:
    obj = xml2json.make_json_from_xml(i, SONG_ID)
    with open(obj['lang'] + '.json', 'w') as f:
        f.write(obj['json'])

with open('info.json', 'w') as f:
    f.write(json.dumps(song_info))


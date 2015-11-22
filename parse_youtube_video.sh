#!/bin/bash
cd data/$1
python ../../get_song_info.py "$1" "$2" "$3" "$4" "$GOOGLE_API_KEY"  #song.json
cd ../

#!/bin/bash
cd data/$1
python ../../get_song_info.py "$GOOGLE_API_KEY" "$1" "$2" "$3" #song.json
cd ../

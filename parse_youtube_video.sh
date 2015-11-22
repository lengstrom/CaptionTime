#!/bin/bash
mkdir data/$1
cd data/$1
python ~/projects/CaptionTime/get_song_info.py "$1" "$2" "$3" "$4" "$GOOGLE_API_KEY"  #song.json
cd ../

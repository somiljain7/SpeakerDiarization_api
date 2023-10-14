#!/bin/bash
cp $1 static/audio.wav
cd /home/coder/Pictures/sd_demo/
if [ -d "data" ]; then
    rm -r data/*
fi

./run_spectral_file.sh --wav_file "$1" --rttm_file "$2"

